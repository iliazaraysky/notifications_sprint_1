FROM python:3.8.5
RUN mkdir /code
COPY /admin_panel/requirements.txt /code
RUN pip install --upgrade pip && pip install -r /code/requirements.txt
COPY /admin_panel /code
WORKDIR /code
CMD gunicorn admin_panel.wsgi:application --bind 0.0.0.0:8000
RUN mkdir static
RUN python manage.py collectstatic
