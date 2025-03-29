from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# File path
file_path = "logs.txt"

# List of names to search for
search_terms = [ "Shreyas Malhotra"]

# Open the file and search for the terms line by line
with open(file_path, "r", encoding="utf-8") as file:
    matches = [line.strip() for line in file if any(term in line for term in search_terms)]

# Create a PDF document
pdf_file = "05.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter

# Title
c.setFont("Helvetica-Bold", 14)
c.drawString(100, height - 40, "Matching Log Entries:")

# Content
c.setFont("Helvetica", 10)
y_position = height - 60

if matches:
    for match in matches:
        c.drawString(100, y_position, match)
        y_position -= 12  # Move down for the next line
        if y_position < 40:  # Check if we need a new page
            c.showPage()
            c.setFont("Helvetica", 10)
            y_position = height - 40
else:
    c.drawString(100, y_position, "No matches found.")

# Save the PDF
c.save()

print(f"PDF saved as {pdf_file}")
