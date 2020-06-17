# pull official base image
FROM python:3.8.0-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install git
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

# Clone repository
RUN git clone https://github.com/nvhnam95/MobileWallet2020 /usr/src/app

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r ./main/requirements.txt

# expose port
EXPOSE 8080

# copy project
COPY . /usr/src/app/

# init database
RUN python main/manage.py makemigrations MobileWallet2020
RUN python main/manage.py migrate

# test
RUN python main/manage.py test
