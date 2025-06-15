#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing requirements..."
pip install django africastalking mysqlclient

echo "Creating requirements.txt..."
pip freeze > requirements.txt

echo "Applying migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Starting server..."
python manage.py runserver
