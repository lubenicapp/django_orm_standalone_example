import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from app.models import User

new_user = User(name='Alice', age=30)
new_user.save()

users = User.objects.all()
for user in users:
    print(user.name, user.age)


user = User.objects.all().delete()
