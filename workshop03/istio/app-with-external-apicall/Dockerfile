FROM python:3-alpine3.9

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app.py app.py

EXPOSE 6000

ENTRYPOINT [ "python", "/app/app.py" ]

