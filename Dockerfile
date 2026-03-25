FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Đặt biến PORT để cloud có thể override
ENV PORT 8001

# Chạy uvicorn dùng biến PORT
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT}"]