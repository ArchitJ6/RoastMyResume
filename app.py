"""
Resume Roast - AI Edition
-------------------------
A Streamlit web application that uses Gemini AI to humorously critique resumes.
The app includes user authentication and supports PDF/TXT resume uploads.

Main Features:
- User registration and authentication with secure password hashing
- PDF and TXT file upload and processing
- AI-powered resume roasting using Google's Gemini model
- Simple and intuitive web interface using Streamlit
"""

import streamlit as st
import PyPDF2
from auth import authenticate, save_user
from process import roast_resume

# =============================
# Main Application UI and Logic
# =============================

def main():
    """Main function that sets up the Streamlit UI and handles user interaction."""
    
    st.title("Resume Roast - AI Edition")
    
    # Initialize session state for tracking the current view
    if "view" not in st.session_state:
        st.session_state.view = "login"  # Default view is login
    
    # Show authentication page if not logged in
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Login")
            login_username = st.text_input("Username", key="login_username")
            login_password = st.text_input("Password", type="password", key="login_password")
            
            if st.button("Login"):
                if not login_username or not login_password:
                    st.error("Please provide both username and password to login")
                else:
                    if authenticate(login_username, login_password):
                        st.session_state["authenticated"] = True
                        st.session_state["username"] = login_username
                        st.rerun()
                    else:
                        st.error("Invalid username or password")
        
        with col2:
            st.subheader("Sign Up")
            signup_username = st.text_input("Choose Username", key="signup_username")
            signup_password = st.text_input("Choose Password", type="password", key="signup_password")
            
            if st.button("Sign Up"):
                if signup_username and signup_password:  # Basic validation
                    save_user(signup_username, signup_password)
                    st.success("Signup successful! Please login.")
                else:
                    st.error("Please provide both username and password")

        # Add "Continue as Guest" option
        st.markdown("---")  # Separator for better UI
        if st.button("Continue as Guest"):
            st.session_state["authenticated"] = True
            st.session_state["username"] = "Guest"
            st.rerun()
    
    # Show main application only after authentication
    else:
        # Show welcome message and logout button in a horizontal layout
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"Welcome, {st.session_state.get('username', '')}! 👋")
        with col2:
            if st.button("Logout"):
                st.session_state.clear()
                st.rerun()
        
        st.write("---")  # Divider
        
        # Main application content
        st.write("Upload your resume and let AI roast it! 🔥")
        uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", 
                                       type=["pdf", "txt"])
        
        if uploaded_file:
            resume_text = ""
            
            # Handle PDF files
            if uploaded_file.type == "application/pdf":
                try:
                    pdf_reader = PyPDF2.PdfReader(uploaded_file)
                    resume_text = []
                    for page in pdf_reader.pages:
                        text = page.extract_text()
                        # Clean up the text: normalize spaces
                        text = ' '.join(text.split())
                        resume_text.append(text)
                    resume_text = '\n\n'.join(resume_text)
                except Exception as e:
                    st.error(f"Error reading PDF: {str(e)}")
            
            # Handle TXT files
            else:
                resume_text = uploaded_file.read().decode("utf-8")

            # Process the resume if we have content
            if resume_text:
                if st.button("Roast my resume"):
                    with st.spinner("Roasting in progress..."):
                        roast_result = roast_resume(resume_text)
                        st.subheader("🔥 AI's Roast of Your Resume 🔥")
                        st.write(roast_result)

# ============================
# Main Application Entry Point
# ============================

if __name__ == "__main__":
    main()