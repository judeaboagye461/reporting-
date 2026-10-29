FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY reporting.py .
COPY test_reporting.py .
COPY app.py .
COPY test_app.py .
COPY database.py .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]