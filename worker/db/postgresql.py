import os
import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

load_dotenv()

dsn = {
    'dbname': os.getenv('POSTGRESQL_DB'),
    'user': os.getenv('POSTGRESQL_USER'),
    'password': os.getenv('POSTGRESQL_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}


def connect_to_db(query, data):
    with psycopg2.connect(dsn=dsn, cursor_factory=DictCursor) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, data)
            result = [dict(row) for row in cursor.fetchall()]
    return result
