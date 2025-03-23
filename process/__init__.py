from config import genai

# =======================
# AI Processing Functions
# =======================

def roast_resume(resume_text: str) -> str:
    """
    Process resume text through Gemini AI for a humorous critique.

    Args:
        resume_text (str): The text content of the resume to analyze

    Returns:
        str: AI-generated humorous critique of the resume
    """
    prompt = f"""Roast my resume in a fun, sarcastic, and brutally honest way. 
            Pretend I'm your friend, and feel free to be a bit dark and mature with the humor. 
            Keep it cringe-worthy, casual, and add in some dad jokes if they fit. 
            Don't hold back—make it simple, sharp, and to the point, with a total word count under 150. 
            My Resume:
            {resume_text}"""
    
    # Initialize and use the Gemini AI model
    model = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")
    response = model.generate_content(prompt)
    return response.text if response else "No response from AI."