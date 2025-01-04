import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()  # Load all environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey, act like a skilled or very experienced ATS (Application Tracking System) with a deep understanding of the tech field, software engineering, data science, data analytics, and big data engineering. Your task is to evaluate the resume based on the given job description. You must consider that the job market is highly competitive, and you should provide the best assistance for improving resumes. Assign the percentage match based on the job description and identify the missing keywords with high accuracy.

resume:{text}
description:{jd}

I want the response in one single string in the structure:
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
"""

# Streamlit App
st.title("Smart ATS")
st.subheader("Improve Your Resume's ATS Score")
st.text("Boost your chances by improving your resume to match job descriptions!")

jd = st.text_area("Paste the Job Description", height=200)
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf", help="Please upload your resume as a PDF file.")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        # Extract text from the uploaded resume
        text = input_pdf_text(uploaded_file)
        
        # Construct the final input for the model
        formatted_prompt = input_prompt.format(text=text, jd=jd)
        
        # Get response from Gemini model
        response = get_gemini_response(formatted_prompt)
        
        try:
            # Parse the response into a structured dictionary
            response_json = json.loads(response)
            
            # Display the results in an attractive format
            st.subheader("ATS Evaluation Results")

            # JD Match (percentage)
            st.markdown(f"**JD Match**: {response_json['JD Match']}")

            # Missing Keywords
            missing_keywords = ", ".join(response_json['MissingKeywords'])
            st.markdown(f"**Missing Keywords**: {missing_keywords if missing_keywords else 'None'}")

            # Profile Summary
            st.markdown("**Profile Summary**:")
            st.text_area("Suggested Profile Summary", value=response_json['Profile Summary'], height=150)
        
        except json.JSONDecodeError:
            st.error("Error processing the response from the model. Please try again.")
    else:
        st.warning("Please upload a PDF resume.")
