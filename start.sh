#!/bin/bash

# start django
python manage.py collectstatic --noinput
python manage.py makemigrations --settings=testsettings
python manage.py migrate --settings=testsettings
python manage.py test vsc --settings=testsettings
python manage.py runserver --settings=testsettings
#gunicorn vsc_app.wsgi -b 0.0.0.0:8000
