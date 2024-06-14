import os
import django
from django.db import connection


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

# For select query, use User.objects.raw()


def create_user(name, age):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO app_user (name, age) VALUES (%s, %s)", [name, age])


def update_user_age(name, new_age):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE app_user SET age = %s WHERE name = %s", [new_age, name])


def delete_user(name):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM app_user WHERE name = %s", [name])
