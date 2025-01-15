FROM python:3.13

WORKDIR /app/

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "main:app", "--workers", "4", "--bind", "0.0.0.0:8000", "--worker-class", "uvicorn.workers.UvicornWorker"]
