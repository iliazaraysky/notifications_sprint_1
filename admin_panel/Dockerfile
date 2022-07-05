FROM python:3.8.5
RUN mkdir /code
COPY /admin_panel/requirements.txt /code
RUN apt-get update && apt-get install -y postgresql-client
RUN pip install --upgrade pip && pip install -r /code/requirements.txt
COPY /admin_panel /code
WORKDIR /code
RUN mkdir static
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
