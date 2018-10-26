FROM python:3.6.2

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 4000

ENV NAME helloworld
ENTRYPOINT ["python", "app.py"]
