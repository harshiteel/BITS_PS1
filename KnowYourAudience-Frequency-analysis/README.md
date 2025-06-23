### Smart Course Chatbot

An AI-powered educational chatbot that answers course-specific questions, analyzes student interactions, determines their skill level, and suggests future questions — all based on PDF course material.

---

### Features

* Upload or select course PDFs
* Ask questions and get answers using Google Gemini
* Store all interactions in Supabase with topic & type metadata
* Classify questions as Fact / Memory / Reasoning
* Analyze most frequent topics and question types
* Judge user's learning level (Beginner, Intermediate, Advanced)
* Generate future questions based on learning pattern

---


### ⚙️ Setup Instructions

1. **Clone the Repository**

2. **Install Dependencies**

3. **Set Up Environment Variables**

   Create a `.env` file:

   ```env
   SUPABASE_URL=your-supabase-url
   SUPABASE_KEY=your-anon-key
   GEMINI_API_KEY=your-gemini-api-key
   ```

4. **Run the App**
   
---

### 🗃️ Supabase Tables

#### `interactions`

Stores each user question and response.

| Column         | Type      |
| -------------- | --------- |
| session\_id    | text      |
| course         | text      |
| question       | text      |
| response       | text      |
| question\_type | text      |
| topic          | text      |
| created\_at    | timestamp |

#### `future_questions`

Stores AI-generated suggested questions.

| Column         | Type      |
| -------------- | --------- |
| session\_id    | text      |
| course         | text      |
| question       | text      |
| topic          | text      |
| question\_type | text      |
| created\_at    | timestamp |
