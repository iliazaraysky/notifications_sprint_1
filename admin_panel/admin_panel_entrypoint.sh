#!/bin/bash

echo "Делаем миграции базы данных"

while ! python manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 1
done

while ! python manage.py makemigrations  2>&1; do
   echo "Migration is in progress status"
   sleep 1
done

echo "Создаем супер пользователя"

while ! python manage.py createsuperuser --noinput --username admin --email example@test.com  2>&1; do
   echo "Migration is in progress status"
   sleep 1
done

echo "Собираем статику"

while ! python manage.py collectstatic 2>&1; do
   echo "Migration is in progress status"
   sleep 2
done

exec "$@"