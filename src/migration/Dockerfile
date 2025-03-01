FROM python:3.10-slim

WORKDIR /app

COPY migration/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY migration/src/ ./src/

CMD ["python", "-u", "-m", "src.migrator"]