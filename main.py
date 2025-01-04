import streamlit as st
import PyPDF2
import requests
from PIL import Image
from io import BytesIO

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to summarize text using the API
def summarize_text(text):
    api_url = "YOUR_API_ENDPOINT"  # Replace with your actual API URL
    headers = {"Content-Type": "application/json"}
    data = {"text": text}
    
    response = requests.post(api_url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("summary", "Error: Summary not found.")
    else:
        return "Error: Unable to summarize."

# Streamlit UI
st.title("PDF Summarizer Web App")

# PDF upload
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
if uploaded_file is not None:
    # Extract text from the PDF
    text = extract_text_from_pdf(uploaded_file)
    
    # Display extracted images
    try:
        # Show the first page as an image (if available)
        image = Image.open(BytesIO(uploaded_file.read()))
        st.image(image, caption="Uploaded PDF Image", use_column_width=True)
    except Exception as e:
        st.write(f"Error displaying image: {e}")

    st.subheader("Extracted Text")
    st.write(text)

    # Summarize Text Button
    if st.button("Summarize Text"):
        if text:
            summary = summarize_text(text)
            st.subheader("AI Summary")
            st.write(summary)
        else:
            st.warning("No text extracted from the PDF.")
