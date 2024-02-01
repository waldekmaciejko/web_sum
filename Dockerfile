# syntax=docker/dockerfile:1
FROM python:3.9.18-slim-bullseye
LABEL maintainer="waldekmaciejko"   
WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
RUN python -m spacy download pl_core_news_sm 
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
