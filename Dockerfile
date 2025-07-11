FROM python:3.11-slim
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt ./models/modelo_demanda.pkl ./models/features.pkl ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "back:app", "--host", "0.0.0.0", "--port", "8000"]