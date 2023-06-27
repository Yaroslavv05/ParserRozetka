import os
import django
from django.conf import settings


def load():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wines_project.settings')
    if not settings.configured:
        django.setup()