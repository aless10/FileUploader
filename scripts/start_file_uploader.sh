#!/bin/bash

# Import the environment vars
export $(egrep -v '^#' .env | xargs)

cd "${PYTHONPATH}"

python /app/file_uploader/manage.py makemigrations
python /app/file_uploader/manage.py migrate
python /app/file_uploader/manage.py createsuperuser --no-input
python /app/file_uploader/manage.py collectstatic --no-input

DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE}" gunicorn file_uploader.wsgi:application --bind 0.0.0.0:8000