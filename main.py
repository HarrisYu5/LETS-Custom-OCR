import pytesseract
from PIL import Image
import pandas as pd
import os

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # Update this path based on your installation


image_path = 'input/1.png'  
img = Image.open(image_path)

# Perform OCR on the image
ocr_text = pytesseract.image_to_string(img, config='--psm 6')
print("OCR Text:", ocr_text)  # Print OCR text for debugging
lines = ocr_text.splitlines()

# Filter out empty lines
cleaned_lines = [line for line in lines if line.strip()]

# Parse the structured lines into a DataFrame (adjust columns based on your table structure)
data = []
for line in cleaned_lines:
    parts = line.split(maxsplit=4)  # Split into 5 parts to match column structure

    mac_address = parts[0]
    ip_address = parts[1]

    # Append parsed data as a new row
    data.append([ mac_address, ip_address])

# Create DataFrame with the specified column structure
df = pd.DataFrame(data, columns=[ "MAC Address", "IP Address"])

# Ensure the output directory exists
os.makedirs('output', exist_ok=True)

# Save DataFrame to an Excel file
output_path = 'output/extracted_data.xlsx'
df.to_excel(output_path, index=False)

print(f"Data saved to {output_path}")