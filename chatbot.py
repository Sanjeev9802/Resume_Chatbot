# AI Career Coach Chatbot using Streamlit + Gemini API

import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
import PyPDF2

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel('models/gemini-2.0-flash')

# --- Helper Functions ---
def extract_text_from_pdf(uploaded_file):
    """Extract text content from uploaded PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return None

def get_resume_feedback(resume_text):
    """Generate professional resume feedback using Gemini"""
    prompt = f"""
    Analyze the following resume and provide professional feedback. 
    Focus on:
    1. Content quality and relevance
    2. Formatting and structure
    3. Skills presentation
    4. Project descriptions
    5. Career path recommendations
    6. Areas for improvement
    
    Please provide specific, actionable suggestions.

    Resume Content:
    {resume_text}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating feedback: {str(e)}"

def generate_roadmap(goal):
    """Generate a comprehensive career roadmap using Gemini"""
    prompt = f"""
    Create a detailed learning and career roadmap for someone who wants to become a {goal}. 
    
    Please include:
    1. Essential skills and technologies to learn
    2. Recommended learning sequence (beginner to advanced)
    3. Important tools and frameworks
    4. Relevant certifications
    5. Practice project ideas
    6. Timeline estimates
    7. Job market insights
    8. Salary expectations
    
    Format the response clearly with sections and bullet points where appropriate.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating roadmap: {str(e)}"

def mock_interview(domain):
    """Generate mock interview questions using Gemini"""
    prompt = f"""
    Create a mock technical interview simulation for a {domain} role. 
    
    Please provide:
    1. 5 technical questions (mix of conceptual and practical)
    2. 2 behavioral questions
    3. 1 scenario-based problem-solving question
    
    For each question, also provide:
    - What the interviewer is looking for
    - Key points a good answer should cover
    
    Format this as a realistic interview experience.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating interview questions: {str(e)}"

def get_career_advice(question):
    """Get general career advice using Gemini"""
    prompt = f"""
    As an experienced career coach, please provide helpful and actionable advice for the following career question:
    
    Question: {question}
    
    Please provide:
    1. Direct answer to the question
    2. Practical steps to take
    3. Additional considerations
    4. Resources or next steps to explore
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating advice: {str(e)}"

# --- Streamlit UI ---
st.set_page_config(
    page_title="AI Career Coach Chatbot", 
    layout="wide",
    page_icon="🧠"
)

st.title("🧠 AI Career Coach Chatbot")

# Sidebar for navigation
st.sidebar.title("🚀 Services")
option = st.sidebar.selectbox(
    "Choose a Service", 
    ["Resume Feedback", "Career Roadmap", "Mock Interview", "Career Advice"]
)

# Check if API key is configured

# Main content based on selected option
if option == "Resume Feedback":
    st.header("📄 Resume Analyzer")
    st.markdown("Upload your resume and get professional feedback to improve your chances!")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Upload your Resume (PDF)", 
            type=["pdf"],
            help="Upload a PDF file of your resume for analysis"
        )
    
    with col2:
        if uploaded_file is not None:
            st.success("✅ Resume uploaded successfully!")
            
            if st.button("🔍 Analyze Resume", type="primary"):
                with st.spinner("🤖 AI is analyzing your resume..."):
                    resume_text = extract_text_from_pdf(uploaded_file)
                    
                    if resume_text:
                        feedback = get_resume_feedback(resume_text)
                        
                        st.subheader("📝 Professional Feedback")
                        st.markdown(feedback)
                        
                        # Option to download feedback
                        st.download_button(
                            label="📥 Download Feedback",
                            data=feedback,
                            file_name="resume_feedback.txt",
                            mime="text/plain"
                        )

elif option == "Career Roadmap":
    st.header("📈 Career Path Generator")
    st.markdown("Get a personalized roadmap for your dream career!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        goal = st.text_input(
            "🎯 Enter your desired role", 
            placeholder="e.g., DevOps Engineer, Data Scientist, Full Stack Developer",
            help="Be specific about the role you want to pursue"
        )
        
        experience_level = st.selectbox(
            "📊 Your current experience level",
            ["Beginner", "Intermediate", "Advanced", "Career Change"]
        )
    
    with col2:
        if goal:
            if st.button("🧭 Generate Roadmap", type="primary"):
                enhanced_prompt = f"{goal} (Current level: {experience_level})"
                
                with st.spinner("🤖 Creating your personalized roadmap..."):
                    roadmap = generate_roadmap(enhanced_prompt)
                    
                    st.subheader("🧭 Your Learning Roadmap")
                    st.markdown(roadmap)
                    
                    # Option to download roadmap
                    st.download_button(
                        label="📥 Download Roadmap",
                        data=roadmap,
                        file_name=f"{goal.replace(' ', '_')}_roadmap.txt",
                        mime="text/plain"
                    )

elif option == "Mock Interview":
    st.header("🎤 Mock Interview Simulator")
    st.markdown("Practice with AI-generated interview questions tailored to your target role!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        domain = st.text_input(
            "💼 Enter your target domain", 
            placeholder="e.g., Frontend Developer, Data Analyst, Cloud Engineer",
            help="Specify the exact role you're preparing for"
        )
        
        interview_type = st.selectbox(
            "🎯 Interview focus",
            ["Technical + Behavioral", "Technical Only", "Behavioral Only"]
        )
    
    with col2:
        if domain:
            if st.button("🚀 Start Interview", type="primary"):
                enhanced_prompt = f"{domain} - {interview_type} focus"
                
                with st.spinner("🤖 Generating interview questions..."):
                    questions = mock_interview(enhanced_prompt)
                    
                    st.subheader("🧪 Interview Questions")
                    st.markdown(questions)
                    
                    # Option to download questions
                    st.download_button(
                        label="📥 Download Questions",
                        data=questions,
                        file_name=f"{domain.replace(' ', '_')}_interview_questions.txt",
                        mime="text/plain"
                    )

elif option == "Career Advice":
    st.header("💡 Career Advice")
    st.markdown("Get personalized career guidance from our AI coach!")
    
    question = st.text_area(
        "❓ What's your career question?",
        placeholder="e.g., How do I transition from marketing to tech? What skills should I focus on for remote work? How do I negotiate salary?",
        height=100,
        help="Ask any career-related question you have"
    )
    
    if question:
        if st.button("🤖 Get Advice", type="primary"):
            with st.spinner("🤖 AI is thinking about your question..."):
                advice = get_career_advice(question)
                
                st.subheader("💬 Career Advice")
                st.markdown(advice)
                
                # Option to download advice
                st.download_button(
                    label="📥 Download Advice",
                    data=advice,
                    file_name="career_advice.txt",
                    mime="text/plain"
                )

# Footer
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
  
    

st.sidebar.markdown("### 🎯 Features")
st.sidebar.markdown("""
- 📄 Resume analysis & feedback
- 📈 Personalized career roadmaps  
- 🎤 Mock interview questions
- 💡 General career advice
- 📥 Download all results
""")