FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev && \
    apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8501"]
