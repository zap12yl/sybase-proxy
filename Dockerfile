# Dockerfile
FROM node:16 AS frontend
WORKDIR /app/frontend
COPY src/webapp/frontend .
RUN npm install
RUN npm run build

FROM python:3.11-slim
WORKDIR /app
COPY --from=frontend /app/frontend/build /app/frontend/build
COPY src/webapp/main.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
