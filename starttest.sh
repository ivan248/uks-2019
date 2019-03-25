#!/bin/bash

# start django in test mode with default DB
python manage.py collectstatic --noinput
python manage.py makemigrations --settings=testsettings
python manage.py migrate --settings=testsettings
python manage.py test vsc --settings=testsettings
