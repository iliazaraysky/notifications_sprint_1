FROM python:3.8.5
RUN mkdir /fastapi
COPY ./api/requirements.txt /fastapi
RUN pip install --upgrade pip && pip install -r fastapi/requirements.txt
COPY ./api /fastapi
WORKDIR /fastapi
CMD ["python", "main.py"]