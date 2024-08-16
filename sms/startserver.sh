#!/bin/sh
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate

echo "Starting the server..."
python manage.py runserver 0.0.0.0:80