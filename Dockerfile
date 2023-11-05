FROM python:3.10

ENV HARISH 1

ADD . /app

WORKDIR /app


COPY /requirements.txt /app/requirements.txtl

RUN pip install -r requirements.txt

CMD ["python","manage","runserver","0.0.0.0:8000"]

# CMD ["python","flask","run","--host:-0.0.0.0"]