FROM python:3.10-slim

WORKDIR /app

COPY EDA.py .
COPY model_training.py .
COPY requirements.txt .
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]

