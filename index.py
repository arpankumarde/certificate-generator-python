# Import the necessary libraries
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Load the certificate template
template = Image.open("templates/certificate.png")

# Optimise the certificate template (If Neccesaary)
# template = template.resize((int(template.width / 8), int(template.height / 8)))

# Load the list of names from an Excel file
names = pd.read_excel("input/attendee-list.xlsx")

# Define the font and size for the names
font = ImageFont.truetype("fonts/Handwind.ttf", 52)

# Loop through the names and generate the certificates
for i, name in enumerate(names["Names"]):
    # Create a copy of the template
    certificate = template.copy()

    # Create a drawing context
    draw = ImageDraw.Draw(certificate)

    # Calculate the position for the name
    w = draw.textlength(name, font=font)
    x = (certificate.width - w) / 2
    y = certificate.height / 2

    # Draw the name on the certificate
    draw.text((x, y), name, font=font, fill=(0, 0, 0))
    certificate = certificate.convert("RGB")

    # Save the certificate
    print(f"Generating certificate {i+1}/{len(names["Names"])}")
    certificate.save(f"certificates/CRT_{i+1}_{name}.pdf")
