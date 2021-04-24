# Using official Python runtime as a parent image.
FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /entityvalidator

# making working directory
WORKDIR /entityvalidator/

# Copying the current directory contents
ADD . /entityvalidator/

RUN pip install -r requirements.txt

EXPOSE 8080

RUN python manage.py migrate

ENTRYPOINT ["python", "manage.py","runserver","0.0.0.0:8080"]