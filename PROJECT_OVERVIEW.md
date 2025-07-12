# BITS Practice School 1 (PS1) - Project Overview

## What is this repository about?

This repository is part of the **BITS Practice School 1 (PS1) internship program** at **AIGurukul Foundation**, focusing on **AI for Education** research and productionization. It tracks the progress of PS1 interns working on various problem statements related to educational AI tools and personalization.

## Main Theme: AI4 Education - Tool Research and Productionisation

The primary focus is leveraging Large Language Models (LLMs) and their emergent capabilities to revolutionize education by:
- Enhancing knowledge dissemination and distillation
- Improving learning personalization 
- Augmenting teacher pedagogy in schools and colleges
- Building upon the existing **VidyaRANG** education personalization platform

## Problem Statement Focus: KnowYourAudience

This repository specifically addresses the **"KnowYourAudience"** problem statement, which involves:
- **Tailoring answers based on learner's qualification and age**
- Implementing the concept of explaining topics at different complexity levels (inspired by "Concept explained in 5 levels")
- Personalizing educational content delivery

## Repository Components

### 1. KnowYourAudience-Quiz
**Purpose**: Interactive quiz application for course-based learning assessment

**Features**:
- AI-generated questions from course PDFs using Google Gemini
- Question categorization: Fact-based, Memory-based, Reasoning-based
- Answer evaluation across correctness, question type, and topic
- Replayable and randomized question experience

**Tech Stack**: Streamlit, Google Gemini, PyPDF2

### 2. KnowYourAudience-Frequency-analysis  
**Purpose**: Smart course chatbot with interaction analysis

**Features**:
- PDF-based course material chatbot
- Question-answer interaction storage in Supabase
- Question classification (Fact/Memory/Reasoning)
- Topic and question type frequency analysis
- User learning level assessment (Beginner/Intermediate/Advanced)
- Future question generation based on learning patterns

**Tech Stack**: Google Gemini, Supabase, PyMuPDF

### 3. KnowYourAudience-Supabase-Analysis
**Purpose**: Student question analysis from database

**Features**:
- Fetches student questions from Supabase database
- AI-powered question topic classification
- User proficiency level evaluation
- Most frequent topic identification

**Tech Stack**: Streamlit, Google Gemini, Supabase

### 4. Team-5-Quiz_and_Chatbot
**Purpose**: Comprehensive smart learning platform combining multiple features

**Features**:
- Course chatbot with PDF-based material
- Interactive practice questions
- User interaction analysis and classification
- Personalized question generation
- Complete learning workflow from chat to practice

**Tech Stack**: Streamlit, Gemini Pro, Supabase, PyMuPDF

## Key Innovation Areas

### 1. **Adaptive Learning**
- Questions and responses tailored to user's demonstrated skill level
- Progressive difficulty adjustment based on interaction patterns

### 2. **Multi-modal Question Types**
- **Fact-based**: Direct information recall
- **Memory-based**: Knowledge retention testing  
- **Reasoning-based**: Critical thinking and application

### 3. **Intelligent Content Analysis**
- PDF parsing and topic extraction
- Automatic content categorization
- Learning pattern recognition

### 4. **Personalization Engine**
- User proficiency classification
- Topic preference identification
- Customized learning path generation

## Research and Development Goals

1. **Research Papers**: Contributing to AI in Education literature
2. **Product Features**: Enhancing VidyaRANG platform capabilities
3. **GenAI Fundamentals**: Deep understanding of generative AI applications
4. **Software Development Skills**: Improving technical implementation capabilities

## Technical Architecture

### Data Flow:
1. **Content Ingestion**: PDF course materials → Text extraction → Topic mapping
2. **User Interaction**: Questions → AI Processing → Response Generation
3. **Analysis**: Interaction Storage → Pattern Recognition → Personalization
4. **Feedback Loop**: User Performance → Difficulty Adjustment → Improved Experience

### Key Technologies:
- **AI/ML**: Google Gemini, Generative AI
- **Database**: Supabase (PostgreSQL-based)
- **Frontend**: Streamlit
- **Document Processing**: PyMuPDF, PyPDF2
- **Environment**: Python, dotenv

## Impact and Applications

This work contributes to the broader **VidyaRANG ecosystem** by:
- Providing personalized learning experiences
- Enabling adaptive content delivery
- Supporting educators with AI-powered tools
- Research insights into effective AI-education integration

## Future Directions

The repository sets the foundation for:
- Integration with the main VidyaRANG platform
- Scaling personalization algorithms
- Enhanced multi-modal learning support
- Real-time adaptive learning systems

---

*This repository represents the collective effort of BITS PS1 interns working towards revolutionizing education through AI-powered personalization and adaptive learning technologies.*