# Проектная работа 10 спринта
![Сервис нотификации](/notification_schema.png "Спринт 10")

**Ссылка на проект:** https://github.com/iliazaraysky/ugc_sprint_2

Перед запуском, необходимо переименовать все файлы типа **env.example** в **.env**.
Директории с файлами:

- notification_sprint_1 (root)
- admin_panel
- auth

Полный запуск проекта файлом [docker-compose.yml](docker-compose.yml) в корне

## Authentication with Flask
Для проведения полноценного тестирования был добавлен сервис аутентификации.

После запуска docker-compose делаем POST-запрос для получения токенов:

Тело запроса:
```
{
    "login": "admin",
    "password": "password123"
}
```

Адрес запроса:
```
http://127.0.0.1:5000/auth/v1/login
```
Без access_token, мы будем получать код 401 unauthorized при обращении к адресам FastAPI

## Admin panel
Сервис располагается по адресу:

```
http://127.0.0.1:8000/admin/
```
```
Логин: admin
Пароль: admin
```
## Worker

## Scheduler

## API

Получить все комментарии к фильму
```
http://127.0.0.1:8001/api/v1/films/4d68876e-0632-4d17-b79f-35ba91394598/comments/
```

## RabbitMQ
Веб-версия брокера доступна по адресу:

```
http://127.0.0.1:15672/
```
```
Логин: guest
Пароль: guest
```
