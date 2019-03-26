#!/bin/bash

# start django
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py test vsc
#python manage.py runserver
gunicorn vsc_app.wsgi -b 0.0.0.0:8000
