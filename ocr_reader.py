import pytesseract
from PIL import Image
import platform
import os

# -----------------------------------
# TESSERACT PATH
# -----------------------------------

if platform.system() == "Windows":

    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

else:

    pytesseract.pytesseract.tesseract_cmd = (
        "/usr/bin/tesseract"
    )


def extract_text(image_path):

    if not os.path.exists(image_path):
        return "Image not found"

    image = Image.open(image_path)

    text = pytesseract.image_to_string(
        image,
        config="--oem 3 --psm 6"
    )

    return text