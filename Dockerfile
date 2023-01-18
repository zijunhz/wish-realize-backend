FROM python:3.10-alpine

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
EXPOSE 80

CMD gunicorn wish_back.wsgi --workers 4 --threads 2 --bind=0.0.0.0:80
