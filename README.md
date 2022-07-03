# Проектная работа 10 спринта
**Ссылка на проект:** https://github.com/iliazaraysky/ugc_sprint_2

**Версия не закончена, отправляю на ревью, что успел сделать. Так как не уверен, что делаю правильно**

Перед запуском, необходимо переименовать все файлы типа **env.example** в **.env**.
Директории с файлами:

- notification_sprint_1 (root)
- admin_panel
- auth
- worker

Полный запуск проекта файлом [docker-compose.yml](docker-compose.yml) в корне

## Authentication with Flask
#Authentication-with-Flask

Регистрация пользователя:
```
http://127.0.0.1:5000/auth/v1/registration
```
POST-запрос для получения access_token:

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

## API
Представим, что мы администратор, и можем за кого угодно оставлять комментарии, а также ставить Like =)
Именно поэтому в поле **user_id** мы можем указать любое значение в формате UUID4

Оставить комментарий к фильму
```
http://127.0.0.1:8001/api/v1/films/4d68876e-0631-4d17-b79f-35ba91394598/add-comment
```

Пример запроса для комментария (film_id будет взят из URL)
```
{
    "user_id": "a363d0c9-4011-4f9f-9a73-d4fd54088f1f",
    "comment": "Awesome comment vol. 1"
}
```

Получить все комментарии к фильму
```
http://127.0.0.1:8001/api/v1/films/4d68876e-0632-4d17-b79f-35ba91394598/comments/
```

Поставить Like комментарию (**True** или **False**)
```
http://127.0.0.1:8001/api/v1/films/{film_id}/comments/{comment_id}/like
```

Пример запроса для лайка коментария (**film_id** и **comment_id** будут взяты из URL)
```
{
    "user_id": "a263d0c9-4011-4f9f-9a73-d4fd54088f1f",
    "like": "True"
}
```
После того, как был поставлен Like комментарию, сообщение о событии будет направлено в брокер


## Admin panel
Сервис располагается по адресу:
#Admin-panel-address
```
http://127.0.0.1:8000/admin/
```
```
Логин: admin
Пароль: admin
```

Необходимо создать шаблон и задание.

Когда в Tasks стоит статус **"Поставить на рассылку"**,
worker сканирует новых пользователей и отправляет в брокер сообщения для них


## Worker
Чтобы проверить работу воркера:

**С базой данных:**
1. Необходимо создать несколько новых пользователей через [сервис аутентификации](#Authentication-with-Flask)
2. Создать в [admin_panel](#Admin-panel-address) task и шаблон
3. Запустить [db_consumer](worker/db_consumer.py) а затем [db_extractor.py](worker/db_extractor.py)

**С FastAPI:**
1. Запустить [api_consumer.py](/worker/api_consumer.py)
2. Оставить несколько комментариев:
```
http://127.0.0.1:8001/api/v1/films/4d68876e-0631-4d17-b79f-35ba91394591/add-comment
```
Пример комментария
```
{
    "author": "a263d0c9-4011-4f9f-9a73-d4fd54088f1f",
    "comment": "Awesome comment vol. 1"
}
```
3. Лайкнуть комментарий используя id другого пользователя:
comment id для url можно взять GET-запросом на адрес:
```
http://127.0.0.1:8001/api/v1/films/4d68876e-0631-4d17-b79f-35ba91394591/comments
```
Адрес для лайка комментария
```
http://127.0.0.1:8001/api/v1/films/4d68876e-0631-4d17-b79f-35ba91394591/comments/6f88c77a-3b1c-4ccf-abca-8395a23f77e0/like
```
Пример запроса
```
{
    "user_id": "a263d0c9-4011-4f9f-9a73-d4fd54088f1f",
    "like": "True"
}
```

Данные в брокер попадут сразу после лайка

## RabbitMQ
Веб-версия брокера доступна по адресу:

```
http://127.0.0.1:15672/
```
```
Логин: guest
Пароль: guest
```
