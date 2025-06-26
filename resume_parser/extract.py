# ---- Python script for Resume Parsing ----
import fitz # PyMuPDF: helps with PDF parsing
import os # for file path operations
import json # for JSON operations
import re # regex: helps with finding patterns in text

# Set the path to the PDF file we're testing with
# This assumes the script is in a subdirectory of the project root
base_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(base_dir, "..", "sample_resumes", 'C1061.pdf')

# Debugging lines to check the file path and existence
'''
print("PDF exists?", os.path.exists(pdf_path))
print("PDF path:", pdf_path) 
'''

# Open the PDF file and extract text from it
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    
    for page in doc:
        text += page.get_text()
    
    return text

text = extract_text_from_pdf(pdf_path)  # Extract text from the PDF file

# Function to extract contact info from the text
def extract_contact_info(text):
    email = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', text) # regex for email
    phone = re.findall(r'\+1-\d{3}-\d{4}', text) # regex for phone number in +1-XXX-XXXX format
    return email[0] if email else None, phone[0] if phone else None # return first match or None if not found

email, phone = extract_contact_info(text)  # Extract email and phone number

print(text)
print("Email:", email)
print("Phone:", phone)