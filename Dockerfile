FROM python:3.7-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 80

COPY src /app

CMD ["python3","./app.py"]
