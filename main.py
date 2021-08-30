# Import functions to API
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/images")
async def process_image(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")

    if not extension:
        return "Image must be jpg or png format!"

    payload = {
        "filename": file.filename,
        "text": "",
        "data": "",
        "image_id": ""
    }
    
    return payload
