from typing import Union
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

from ultralytics import YOLO
model = YOLO('best.pt')

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
