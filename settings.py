import django
from django.conf import settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase.db',
    }
}

INSTALLED_APPS = [
    'app',
]

settings.configure(
    DATABASES=DATABASES,
    INSTALLED_APPS=INSTALLED_APPS,
)

django.setup()
