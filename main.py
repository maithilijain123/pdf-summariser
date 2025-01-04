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
<<<<<<< HEAD
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
=======
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
>>>>>>> 16dca0c4722d1fe11490f9a4c93103dacfd2e156

# Streamlit app setup
def main():
    st.title("PDF Summarizer")
    
<<<<<<< HEAD
    # PDF file uploader widget
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if pdf_file is not None:
        # Extract text from the uploaded PDF
=======
    # PDF file uploader
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if pdf_file is not None:
        # Extract text from the PDF
>>>>>>> 16dca0c4722d1fe11490f9a4c93103dacfd2e156
        text = extract_text_from_pdf(pdf_file)
        
        if text:
            st.write("Extracted Text from PDF:")
<<<<<<< HEAD
            st.write(text[:1000])  # Display only first 1000 characters
=======
            st.write(text[:1000])  # Display first 1000 characters
            
            # Summarize text using the API
>>>>>>> 16dca0c4722d1fe11490f9a4c93103dacfd2e156
            summary = summarize_text(text)
            st.write("Summary:")
            st.write(summary)
        else:
            st.write("No text found in the PDF.")
    else:
        st.write("Please upload a PDF file.")

<<<<<<< HEAD
# Running the Streamlit app
=======
# Run the app
>>>>>>> 16dca0c4722d1fe11490f9a4c93103dacfd2e156
if __name__ == '__main__':
    main()
