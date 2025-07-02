from fastapi import FastAPI, File, UploadFile
import pytesseract
from PIL import Image
import io
import pickle
import numpy as np

app = FastAPI()

# Load the fraud detection model
import joblib
model = joblib.load("model.pkl")


@app.get("/")
def read_root():
    return {"message": "Fraud & OCR API is running!"}

@app.post("/predict_fraud/")
def predict_fraud(amount: float, transaction_type: str):
    X = np.array([[amount, 1 if transaction_type.lower() == 'debit' else 0]])
    prediction = model.predict(X)[0]
    return {"fraud_prediction": int(prediction)}

@app.post("/ocr/")
async def extract_text(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))
    text = pytesseract.image_to_string(image)
    return {"extracted_text": text}
