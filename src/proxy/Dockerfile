FROM python:3.10-slim

WORKDIR /app

COPY proxy/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY proxy/src/ ./src/

CMD ["python", "-u", "src/main.py"]
