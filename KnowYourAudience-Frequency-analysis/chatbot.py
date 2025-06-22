import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import streamlit as st
from llama_index.core import SimpleDirectoryReader
import fitz  # PyMuPDF
import pathlib
from supabase import create_client, Client
import uuid

# Load env variables
load_dotenv()

# Supabase Credentials
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url,key)

# Gemini Credentials
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
model = "gemini-2.5-flash-preview-05-20"

# Assign session ID for the user
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Text extraction from PDF
@st.cache_data(show_spinner="Extracting text...")
def extract_pdf_text(file_path):
    doc = fitz.open(file_path)
    texts = []
    for page in doc:
        texts.append(page.get_text())
    return "\n".join(texts)

# Gemini Interactions
def gemini_interact(prompt):
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )
        return response.text
    except Exception as e:
        st.error(f"Error interacting with Gemini: {e}")
        return ""

@st.cache_data(show_spinner=False)
def get_response(question, course_content):
    prompt = f"""Answer the given question based on the document provided. Be short and to the point. 
    
    ---DOCUMENT---
    {course_content}
    ---END---

    Question: {question}
    """
    return gemini_interact(prompt)

def classify_question(question):
    prompt = f"Classify the question as Fact, Reasoning or Memory. Just return the label. \nQuestion: {question}"
    return gemini_interact(prompt).strip().lower()

def extract_topic(question):
    prompt = f"Identify the topic of the question from the document provided in 4-5 words. Just return the topic name.\nQuestion: {question}"
    return gemini_interact(prompt).strip()

def determine_user_level(interactions):
    questions = "\n".join(f"- {i['question']}" for i in interactions)
    prompt = f"""
        You are a tutor assessing a student based on the questions they asked.
        Here are the questions:
        {questions}

        Based on the complexity, topic depth, and reasoning involved, classify the user’s skill level as one of the following:
        Beginner, Intermediate, Advanced.

        Return only:
        Level: <Beginner/Intermediate/Advanced>"""

    result = gemini_interact(prompt)
    return result.strip()

def generate_future_question(most_freq_topic, most_freq_type, user_level):
    prompt = f"""
        Based on the above interactions, generate 3 questions which user might ask in future. The questions should be from 
        {most_freq_topic} and should be {most_freq_type} based. The level of questions should be at par with user level: {user_level}.
        Return as a list with each question on a new line.
        Do not return any other text."""
    raw_response = gemini_interact(prompt)
    if not raw_response:
        return []
    return [q.strip() for q in raw_response.split('\n') if q.strip()]


# Streamlit UI Setup
st.set_page_config(page_title="Course Chatbot", layout="centered")
st.title("Smart Course Chatbot")
st.subheader("Get answers to your course-related questions along with interactive analysis!")

# List of courses with PDF files
courses = {
    "Current Electricity": "courses/current-electricity-ncert.pdf",
    "Ray Optics": "courses/ray-optics-ncert.pdf",
    "Solutions": "courses/solutions-ncert.pdf",
    "Matrices and Determinants": "courses/matrices-ncert.pdf",
}

selected_course = st.selectbox(
        "Select a Course to study!", 
        list(courses.keys()), 
        index=None
    )

def load_chat_history(session_id, course):
    results = supabase.table("interactions").select("*")\
        .eq("session_id", session_id)\
        .eq("course", course)\
        .order("created_at", desc=True)\
        .execute()
    return results.data if results.data else []


if selected_course:
    # st.success(f"✅ {selected_course} selected.")
    course_file = courses[selected_course]
    with open(course_file, "rb") as f:
        course_content = extract_pdf_text(course_file)
    st.session_state.course_content = course_content

    # Load chat history if not already
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = load_chat_history(st.session_state.session_id, selected_course)

    # Show chat history
    if st.session_state.chat_history:
        # st.subheader("🧾 Chat History")
        for chat in st.session_state.chat_history:
            st.markdown(f"**You:** {chat['question']}")
            st.markdown(f"**Bot:** {chat['response']}")
            st.markdown("---")

    # Ask question
    question = st.text_input("Ask a question", key="question_input", placeholder="Type your question here...")

    if st.button("Get Answer"):
        question = st.session_state.question_input
        if question.strip() == "":
                st.warning("Please enter a question.")
        else:
            # Get response from Gemini
            response = get_response(question, course_content)
            question_type = classify_question(question)
            topic = extract_topic(question)

            # Store in Supabase
            supabase.table("interactions").insert({
                "session_id": st.session_state.session_id,
                "course": selected_course,
                "question": question,
                "response": response,
                "question_type": question_type,
                "topic": topic
            }).execute()

            # Update session state chat history
            st.session_state.chat_history.append({
                "question": question,
                "response": response,
                "question_type": question_type,
                "topic": topic
            })

            # Clear question input
            del st.session_state.question_input
            st.rerun()

    st.markdown("---")
    st.subheader("Analysis of Interactions")
    if st.button("🧠 Analyze Interactions"):
        history = st.session_state.chat_history
        if len(history) < 4:
            st.warning("You need at least 4 interactions to analyze.")
        else:
        # Count frequency of topics and question types
            topic_count = {}
            type_count = {}
            user_level = determine_user_level(history)

            for chat in history:
                topic = chat.get("topic", "").strip()
                q_type = chat.get("question_type", "").strip()
                topic_count[topic] = topic_count.get(topic, 0) + 1
                type_count[q_type] = type_count.get(q_type, 0) + 1

            # Find most frequent topic and type
            most_freq_topic = max(topic_count, key=topic_count.get)
            most_freq_type = max(type_count, key=type_count.get)

            st.info(f"\nMost Frequent Topic: {most_freq_topic}")
            st.info(f"\nMost Frequent Question Type: {most_freq_type}")
            st.info(f"\nUser Skill Level: {user_level}")

            # Generate future questions
            future_questions = generate_future_question(most_freq_topic, most_freq_type, user_level)

            # Save each future question to Supabase
            for q in future_questions:
                supabase.table("future_questions").insert({
                    "session_id": st.session_state.session_id,
                    "course": selected_course,
                    "question": q,
                    "topic": most_freq_topic,
                    "question_type": most_freq_type
                }).execute()
            
            st.success("Future questions generated and saved to database.")
