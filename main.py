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
    # Your new API key
    api_key = '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'
    
    # API URL (Replace with your actual endpoint URL)
    api_url = 'https://api.openai.com/v1/completions'  # Example endpoint for OpenAI
    
    headers = {
        'Authorization': f'Bearer {api_key}',  # Adding Bearer token to headers
        'Content-Type': 'application/json'
    }
    
    # Data payload
    data = {
        'model': 'text-davinci-003',  # Example model name for OpenAI GPT-3
        'prompt': text,
        'max_tokens': 500
    }
    
    try:
        # Make the API request
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        summary = response.json().get('choices')[0]['text'].strip()
        return summary
    except requests.exceptions.RequestException as e:
        return f"Error occurred: {e}"

# Streamlit app setup
def main():
    st.title("PDF Summarizer")
    
    # PDF file uploader
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if pdf_file is not None:
        # Extract text from the PDF
        text = extract_text_from_pdf(pdf_file)
        
        if text:
            st.write("Extracted Text from PDF:")
            st.write(text[:1000])  # Display first 1000 characters
            
            # Summarize text using the API
            summary = summarize_text(text)
            st.write("Summary:")
            st.write(summary)
        else:
            st.write("No text found in the PDF.")
    else:
        st.write("Please upload a PDF file.")

# Run the app
if __name__ == '__main__':
    main()
