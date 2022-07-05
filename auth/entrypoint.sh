#!/bin/bash

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$DB_HOST" -U "$POSTGRES_USER" -d "$DB_NAME" -c '\q'; do
  sleep 2
done

flask db upgrade
flask createsuperuser admin password123

gunicorn wsgi_app:app --bind :5000