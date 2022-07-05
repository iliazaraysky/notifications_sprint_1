FROM python:3.8.5
RUN mkdir /app
COPY ./auth/requirements.txt /app
RUN apt-get update && apt-get install -y postgresql-client
RUN pip install --upgrade pip && pip install -r ./app/requirements.txt
COPY . /app
WORKDIR /app/auth
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/app/auth/entrypoint.sh"]
