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

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/linkedin-resume-generator.git
   cd linkedin-resume-generator
2.**Install required packages: Create a virtual environment and install dependencies:**

'''bash
   python3 -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     pip install -r requirements.txt
3.**Run the Streamlit app:**
'''bashgit add README.md
streamlit run app.py
Access the app: Open your browser and go to http://localhost:8501 to access the web app.