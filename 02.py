import PyPDF2
import re

# Path to your PDF file
pdf_file_path = '04.pdf'

# Function to extract text from the PDF
def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to calculate the total kpm
def calculate_total_kpm(text):
    # Regular expression to extract kpm values
    kpm_values = re.findall(r'kpm (\d+)', text)
    kpm_values = [int(kpm) for kpm in kpm_values]
    total_kpm = sum(kpm_values)
    return total_kpm

# Extract text from PDF
text = extract_text_from_pdf(pdf_file_path)

# Calculate total kpm
total_kpm = calculate_total_kpm(text)

print(f"Total kpm (sum of kpm values): {total_kpm}")
