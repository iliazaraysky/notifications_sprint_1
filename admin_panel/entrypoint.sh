#!/bin/bash

until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c '\q'; do
  sleep 2
done

python3 manage.py migrate
python3 manage.py collectstatic --no-input
python3 manage.py createsuperuser --noinput --username admin --email example@test.com

gunicorn admin_panel.wsgi:application --bind 0.0.0.0:8000