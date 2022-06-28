FROM python:3.8.5
RUN mkdir /code
COPY /admin_panel/requirements.txt /code
RUN pip install --upgrade pip && pip install -r /code/requirements.txt
COPY /admin_panel /code
WORKDIR /code
RUN mkdir static
RUN chmod +x admin_panel_entrypoint.sh
ENTRYPOINT ["/code/admin_panel_entrypoint.sh"]