import json
import os
import psycopg2
import pika
from dotenv import load_dotenv

load_dotenv()

dsn = {
    'host': os.getenv('DB_HOST'),
    'dbname': os.getenv('POSTGRESQL_DB'),
    'user': os.getenv('POSTGRESQL_USER'),
    'password': os.getenv('POSTGRESQL_PASSWORD'),
    'port': os.getenv('DB_PORT')
}
#
connection = psycopg2.connect(**dsn)
cursor = connection.cursor()


def add_task_to_queue(data):
    task = check_tasks_from_admin_panel()
    id = task[0][1]
    status = task[0][1]
    message = task[0][2]

    connection_parametrs = pika.ConnectionParameters(host="localhost", port=5672)
    connection = pika.BlockingConnection(connection_parametrs)
    channel = connection.channel()
    channel.queue_declare(queue='email')

    for user_data in data:
        user_id = user_data[0]
        user_name = user_data[1]
        user_email = user_data[2]
        message_dictionary = {
            'user_id': user_id,
            'user_name': user_name,
            'user_email': user_email,
            'message': message
        }
        message_json = json.dumps(message_dictionary)
        channel.basic_publish(
            exchange='',
            routing_key='email',
            body=message_json
        )
    connection.close()


def selection_for_new_users():
    cursor.execute("SELECT id, name, email FROM users WHERE created >= NOW() - INTERVAL '24 HOURS'")
    result = cursor.fetchall()
    return result


def check_tasks_from_admin_panel():
    cursor.execute("SELECT mailing_list_tasks.id, status, text"
                   " FROM mailing_list_tasks"
                   " INNER JOIN notification_templates"
                   " ON mailing_list_tasks.template_id=notification_templates.id"
                   " WHERE status='send'")
    result = cursor.fetchall()
    return result

add_task_to_queue(selection_for_new_users())
