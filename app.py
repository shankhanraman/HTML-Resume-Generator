import streamlit as st
import PyPDF2
import openai

# Set page config and style
st.set_page_config(page_title="PDF to HTML Resume Generator", page_icon=":memo:", layout="centered")
st.markdown(
    """
    <style>
        .main {
            background-color: #1e1e1e; /* Darker background */
            color: #f5f5f5; /* Light text for better contrast */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stButton button {
            background-color: #333333; /* Darker button */
            color: #ffffff; /* White text for contrast */
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
            border: 2px solid #4CAF50; /* Green border for emphasis */
        }
        .stButton button:hover {
            background-color: #4CAF50; /* Hover effect to green */
        }
        .stTextInput input {
            background-color: #2b2b2b; /* Darker input field */
            color: #ffffff; /* White text in input */
            border-radius: 10px;
            border: 1px solid #4CAF50; /* Green border */
            padding: 10px;
        }
        .stFileUploader {
            background-color: #2b2b2b; /* Dark file uploader */
            color: #ffffff;
            border-radius: 10px;
            border: 1px solid #4CAF50;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #4CAF50; /* Green headings */
        }
        .css-1d391kg {
            background-color: #2b2b2b !important; /* Dark select widget */
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Add a title and description
st.title(":memo: LinkedIn PDF to HTML Resume Generator")
st.write(
    """
    Convert your LinkedIn resume (PDF) into a structured, professional HTML format using AI. Follow the steps below to upload your resume, provide your OpenAI API key, and download your HTML resume.
    """
)

# Step-by-step guide
st.markdown("### Step 1: Upload your LinkedIn PDF")

# Upload LinkedIn PDF
uploaded_file = st.file_uploader("Upload your LinkedIn resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")
    # Extract text from PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    # Show a preview of the extracted text (optional)
    with st.expander("Show extracted text from PDF"):
        st.text_area("PDF Text", value=pdf_text, height=200)

# Get OpenAI API Key
st.markdown("### Step 2: Enter your OpenAI API key")
api_key = st.text_input("Enter your OpenAI API key:", type="password")

if api_key and uploaded_file:
    # Generate HTML Resume
    st.markdown("### Step 3: Generate HTML Resume")
    if st.button("Generate HTML"):
        with st.spinner("Generating HTML..."):
            openai.api_key = api_key
            # Call OpenAI to transform PDF text into HTML
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Convert this resume to HTML: {pdf_text}",
                max_tokens=2000
            )
            generated_html = response['choices'][0]['text']

            # Display the generated HTML
            st.markdown("### Step 4: Download Your HTML Resume")
            st.markdown(generated_html, unsafe_allow_html=True)

            # Provide a download button for HTML file
            st.download_button("Download HTML Resume", generated_html, file_name="resume.html")
else:
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    if not uploaded_file:
        st.warning("Please upload a PDF first.")
