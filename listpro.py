from fpdf import FPDF

def create_pdf_from_text(text_content, filename="computer_vision_projects.pdf"):
    """
    Generates a PDF file from a string of text.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=14)

    # Get the effective page width for calculations
    effective_page_width = pdf.w - pdf.l_margin - pdf.r_margin

    # Split the text content by line and add to the PDF
    for line in text_content.split('\n'):
        line = line.strip() # Remove leading/trailing whitespace

        if not line: # Skip empty lines
            continue
        
        # Differentiate between titles and list items
        if line.startswith('###'):
            pdf.set_font("Helvetica", 'B', 16) # Set bold font for sections
            pdf.ln(10) # Add extra spacing before a new section
            # Use effective_page_width for the width to avoid calculation errors
            pdf.multi_cell(effective_page_width, 10, line.replace('### ', ''))
            pdf.ln(5)
            pdf.set_font("Helvetica", size=14) # Revert to normal font
        elif line.startswith('*'):
            # Format list items with a bullet and handle text wrapping
            # Use an explicit width for the multi_cell
            bullet_text = line.replace('*   ', '')
            pdf.multi_cell(effective_page_width, 8, bullet_text, align='L')
        else:
            # Handle other lines with the full page width
            pdf.multi_cell(effective_page_width, 8, line)

    pdf.output(filename)
    print(f"PDF saved to '{filename}'")

# The content to be written to the PDF file
projects_text = """
### Object and shape detection
*   Real-time QR and Barcode Scanner*
*   Simple Object Counter*
*   Handwritten Digit Recognition*
*   Color Detection and Tracking*
*   License Plate Recognition
*   Custom Object Detection with YOLO*
*   Car Park Space Detection
*   Road Sign Detection

### Face and body analysis
*   Face Detection and Blur Filter*
*   Drowsiness and Yawn Detection*
*   Hand Gesture Volume Control*
*   Hand Controlled Game (e.g., virtual Rock-Paper-Scissors)*
*   Hand Landmark Detection and Recognition
*   Real-Time Body Pose Estimation
*   Facial Emotion Recognition
*   Facial Landmark Detection

### Image processing
*   Real-time Video Sketch Filter*
*   Basic Image Filters (Blur, Sharpen, Grayscale)*
*   Document Scanner*
*   Background Removal
*   Create Panoramic Image Stitching
*   Image Colorization

### Text and data extraction
*   Optical Character Recognition (OCR)*
*   Traffic Sign Recognition
*   Handwritten Character Recognition
*   License Plate Text Extraction

### Practical applications
*   Simple Lane Detection
*   Intruder Detection System*
*   Food Calorie Estimation
*   Smart Attendance System (using face recognition)
*   Object Counter for Video Surveillance

### Interactive and fun
*   Virtual Paint Application*
*   Chrome Dino Game Bot (using screen capture)*
*   "Invisible" Cloak (based on color tracking)*
*   Real-time Object Measurement*
"""

if __name__ == "__main__":
    create_pdf_from_text(projects_text)
