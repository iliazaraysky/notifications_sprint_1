FROM python:3.8.5
RUN mkdir /app
COPY ./auth/requirements.txt /app
RUN pip install --upgrade pip && pip install -r ./app/requirements.txt
COPY . /app
WORKDIR /app/auth
CMD ["gunicorn", "wsgi_app:app", "--bind", ":5000"]
