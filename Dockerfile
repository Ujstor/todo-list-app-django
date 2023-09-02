FROM python:3.9.18

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x django.sh

ENTRYPOINT ["/app/django.sh"]