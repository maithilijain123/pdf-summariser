import streamlit as st
import requests
import PyPDF2

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to summarize text using an API
def summarize_text(text):
    # Replace this with your actual API endpoint
    api_url = 'https://api.openai.com/v1/completions'  # OpenAI API endpoint example
    
    # Your API key
    api_key = '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'

    # Data format for the request
    data = {
        "model": "text-davinci-003",  # Or whatever model you are using (like GPT-3)
        "prompt": text,
        "max_tokens": 1000  # Adjust as per your needs
    }
    
    # Headers for the API request
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    try:
        # Sending POST request to the API
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        
        # Extracting summary from the response
        summary = response.json().get('choices')[0].get('text').strip()
        return summary
    
    except requests.exceptions.RequestException as err:
        return f"Error occurred: {err}"

# Streamlit app setup
def main():
    st.title("PDF Summarizer")
    
    # PDF file uploader widget
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if pdf_file is not None:
        # Extract text from the uploaded PDF
        text = extract_text_from_pdf(pdf_file)
        
        if text:
            st.write("Extracted Text from PDF:")
            st.write(text[:1000])  # Display only first 1000 characters
            summary = summarize_text(text)
            st.write("Summary:")
            st.write(summary)
        else:
            st.write("No text found in the PDF.")
    
    else:
        st.write("Please upload a PDF file.")

# Running the Streamlit app
if __name__ == '__main__':
    main()
