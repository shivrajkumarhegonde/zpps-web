#!/bin/sh
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate

echo "Starting the server..."
gunicorn sms.wsgi:application --bind 0.0.0.0:10000