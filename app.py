import streamlit as st

from dotenv import load_dotenv
load_dotenv()

import os
from PyPDF2 import PdfReader
import google.generativeai as genai

##key exports from .env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))




##model response
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input, pdf_content, prompt])
    return response.text



##pdf to text
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        text=""
        pdf_reader= PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text+= page.extract_text()

        return text
    else:
        raise FileNotFoundError("No file uploaded")









## Streamlit App

st.set_page_config(page_title="Resume Expert")
st.header("Resume Helper 👍")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])



if uploaded_file is not None:
    st.success("PDF Uploaded Successfully")

    # Use a select slider for different options
    selected_option = st.selectbox(
        'Select an option:',
        options=['Tell Me About the Resume', 'Percentage Match','Suggestion']
    )

    if selected_option == 'Tell Me About the Resume':
        input_prompt = """
        You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
        Please share your professional evaluation on whether the candidate's profile aligns with the role. 
        Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements. You need to read the Resume properly you
        shold not give any wrong answers.
        """
        input_text ="Explain about the resume simple and neat start with candidate name and explain key points"

    elif selected_option == 'Percentage Match':
        input_prompt = """
        You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
        your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
        the job description. First, the output should come as a percentage and then keywords missing and last final thoughts.
        """
        input_text = st.text_area("Job Description: ", key="input")
    else:
        input_prompt="""
                        Based on the resume find the area of interest and their domain and give suggestions based on their
                        domain and resume for them to improve their skills give suugestion based on the content present in the
                        resume and what can they improve
                        """
        input_text="Give Suggestion for me to improve"


    submit = st.button("Submit")





    if submit:
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt, pdf_content, input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload the resume")
