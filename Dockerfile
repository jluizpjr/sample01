# syntax=docker/dockerfile:1


#FROM python:3.8-slim-buster
#FROM python:3.8.10-buster

FROM registry.suse.com/suse/sle15:latest

WORKDIR /app

COPY requirements.txt requirements.txt
#RUN python -m pip install --upgrade pip
RUN python3 --version
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

