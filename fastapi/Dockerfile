FROM python:3.9.15-alpine3.15

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn main:app --reload --host 0.0.0.0 --port 80