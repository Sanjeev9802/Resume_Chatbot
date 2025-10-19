# AI Career Coach Chatbot

An intelligent career guidance platform using Google Gemini API to provide personalized resume analysis, career roadmaps, mock interviews, and professional advice.

## Features
- 📄 **Resume Analysis**: Upload PDF resumes and get AI-powered feedback
- 📈 **Career Roadmap**: Generate personalized learning paths for target roles
- 🎤 **Mock Interview**: Practice with AI-generated interview questions
- 💡 **Career Advice**: Get professional guidance on career decisions

## Tech Stack
Python, Streamlit, Google Gemini API, PyPDF2, python-dotenv

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Sanjeev9802/Resume_Chatbot.git
cd Resume_Chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Gemini API Key
Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### 4. Create `.env` file
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the application
```bash
streamlit run chatbot.py
```

The app will open at `http://localhost:8501`

## License
MIT License
