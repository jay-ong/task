#!/bin/sh

docker-compose build

docker run -d --name task-django-app -p 8000:8000 task-django-app:latest

docker run -d --name task-react-app -p 3000:3000 task-react-app:latest