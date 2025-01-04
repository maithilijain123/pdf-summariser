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
    # Yeh URL apne API ka daalna hai
    api_url = 'https://YOUR_API_ENDPOINT'  # Yeh apne API ka endpoint daalna hai
    data = {'text': text}
    
    # Agar API key chahiye, toh headers mein daalna padega
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY',  # Agar API key chahiye toh yeh daalna
        'Content-Type': 'application/json'
    }
    
    try:
        # API ko request bhejna
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()  # Agar kuch galat hua, toh error aayega
        summary = response.json().get('summary', 'No summary found')  # Summary nikaalna
        return summary
    except requests.exceptions.RequestException as err:
        return f"Error occurred: {err}"

# Streamlit app setup
def main():
    st.title("PDF Summarizer")
    
    # PDF upload karne ka option dena
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    if pdf_file is not None:
        # PDF ka text extract karna
        text = extract_text_from_pdf(pdf_file)
        
        if text:
            st.write("Extracted Text from PDF:")
            st.write(text[:1000])  # Sirf 1000 characters ka preview dikhana
            # Summary banana
            summary = summarize_text(text)
            st.write("Summary:")
            st.write(summary)
        else:
            st.write("No text found in the PDF.")
    
    else:
        st.write("Please upload a PDF file.")

if __name__ == '__main__':
    main()
