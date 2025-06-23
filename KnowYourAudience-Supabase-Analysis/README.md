## Supabase Analysis 

A Streamlit-based app that fetches student questions from a **Supabase database**, uses **Google Gemini** to classify each question by **topic**, and evaluates the **user's overall level** (Beginner, Intermediate, or Advanced). It also identifies the **most frequent topic** asked by the user.

---

### Features

* **Fetch questions** from a Supabase table
* **Classify each question by topic** using Gemini
* **Determine user level** based on question complexity and type
* **Identify most frequent topic** asked

---

### ⚙️ Setup Instructions

1. **Clone the Repository**

2. **Install Dependencies**

3. **Configure Environment Variables**

Create a `.env` file:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
GEMINI_API_KEY=your_gemini_api_key
```

4. **Run the App**

---

### Supabase Table Schema

**course_chat_logs**

| Column    | Type            |
| --------- | --------------- |
| user\_id  | uuid            |
| chat_history | jsonb        |

