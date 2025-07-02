# 🛡️ Mini-Gateway Fraud & OCR Detection API

This project is a **FastAPI-based fraud detection and OCR microservice**, containerized using Docker. The ML model predicts fraudulent transactions based on features, and the OCR module extracts data from receipt images.

---

## 🚀 Features
- Fraud prediction using a trained `RandomForestClassifier`
- Receipt OCR parsing (Tesseract or similar)
- Real-time API served via FastAPI (Swagger UI)
- Dockerized for easy deployment
- Model saved in `model.pkl`

---

## 📊 Model Evaluation

| Metric         | Value          |
|----------------|----------------|
| PR-AUC         | *e.g., 0.87*   |
| Recall @ 0.5% FPR | *e.g., 0.61* |

Class imbalance was handled using **SMOTE**, and feature engineering involved domain-driven feature selection.

---

## 🧠 OCR Notes

OCR errors are reduced by:
- Using regex-based field cleaning
- Running Levenshtein distance on misreads
- Ignoring malformed receipts

---

## 🛠️ Setup & Run

### 1. Build Docker Image

```bash
docker build -t fraud-ocr-app .
