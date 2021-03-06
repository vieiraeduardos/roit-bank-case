# Import functions to database
from models.Images import Images

# Import funtions to process images
import numpy as np
import cv2
from PIL import Image
from io import BytesIO
import base64
import pytesseract

# Import functions to API
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# Convert image to numpy array
def read_image(file):
    image = Image.open(BytesIO(file))
    return image

# Clean noises from image 
def clean_image(image):
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    denoise_2 = cv2.fastNlMeansDenoisingColored(img,None,5,5,7,21) 
    
    return denoise_2

# Return text extracted from image
def get_ocr_from_image(image):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'

    result = pytesseract.image_to_string(image, lang="eng")

    return result


@app.post("/images")
async def process_image(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")

    if not extension:
        return "Image must be jpg or png format!"

    formatted_image = read_image(await file.read())

    cleaned_image = clean_image(formatted_image)

    text = get_ocr_from_image(cleaned_image)

    encoded_image = base64.b64encode(cleaned_image)

    img = Images(file.filename, text, encoded_image)

    image_id = img.insert()

    payload = {
        "filename": file.filename,
        "text": text,
        "data": encoded_image,
        "image_id": str(image_id)
    }
    
    return payload