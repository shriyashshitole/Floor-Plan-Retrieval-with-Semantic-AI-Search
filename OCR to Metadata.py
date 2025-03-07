import os
import json
import cv2
import pytesseract
import re

# Set the correct path for Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Path to images
IMAGE_FOLDER = "floor_plans"
OUTPUT_METADATA = "floor_plan_metadata.json"

# Function to extract room dimensions and estimate square footage
def extract_dimensions(text):
    pattern = re.compile(r'(\d+)-(\d+) x (\d+)-(\d+)')  # Matches "12-2 x 13-8"
    matches = pattern.findall(text)
    
    total_sqft = 0
    for match in matches:
        width = int(match[0]) + int(match[1]) / 12
        height = int(match[2]) + int(match[3]) / 12
        total_sqft += width * height
    return total_sqft

# Process all images
metadata = []
for filename in os.listdir(IMAGE_FOLDER):
    if filename.endswith((".jpg", ".png")):
        image_path = os.path.join(IMAGE_FOLDER, filename)
        
        # Read and extract text
        image = cv2.imread(image_path)
        extracted_text = pytesseract.image_to_string(image)

        # Estimate total area
        sqft_estimate = extract_dimensions(extracted_text)

        # Store metadata
        metadata.append({
            "file_path": image_path,
            "extracted_text": extracted_text,
            "estimated_sqft": sqft_estimate
        })

# Save metadata to JSON
with open(OUTPUT_METADATA, "w") as f:
    json.dump(metadata, f, indent=4)

print(f" Metadata saved to {OUTPUT_METADATA}")


