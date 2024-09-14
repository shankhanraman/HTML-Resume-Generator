# LinkedIn PDF to HTML Resume Generator

This web application, built using **Streamlit**, allows users to convert their LinkedIn PDF resumes into a structured, professional HTML format using OpenAI's API.

## Features
- **PDF Upload**: Upload your LinkedIn resume in PDF format.
- **OpenAI Integration**: Automatically generate an HTML resume from the uploaded PDF using OpenAI's API.
- **Download HTML**: Download the generated HTML resume.
- **Dark Mode UI**: The application features a clean, dark-themed user interface for better visibility.

## Prerequisites
- Python 3.7 or above
- OpenAI API Key (for interacting with GPT-3)

## Problem Solved
The main challenge addressed was converting a LinkedIn PDF resume into a structured HTML resume. To convert LinkedIn PDF resumes into HTML format, we used the following approach and methods:

1. **PDF Extraction**:
   - **PDF Parsing**: Used `PyPDF2` to extract text from the uploaded PDF resume. This library helps in reading the content of the PDF, including sections like education, experience, and skills.

2. **Text Processing**:
   - **OpenAI **: Utilized OpenAI's  API to process and format the extracted text into HTML. This involved sending the extracted resume content to GPT-3 for conversion into a well-structured HTML format.

3. **User Interface**:
   - **Streamlit**: Developed the web interface using Streamlit. This framework provides an easy way to create interactive web applications with a clean, dark-themed UI for better readability and user experience.

4. **Deployment**:
   - **Vercel**: Deployed the Streamlit application on Vercel for easy access and sharing. This involved configuring the Vercel deployment settings to run the Streamlit app and handle file uploads.


## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/linkedin-resume-generator.git
   cd linkedin-resume-generator
2. **Install required packages: Create a virtual environment and install dependencies:**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   Access the app: Open your browser and go to http://localhost:8501 to access the web app.
 
