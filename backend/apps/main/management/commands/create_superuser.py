import os

from apps.routines.models import *
from apps.customers.models import *
from apps.main.models import *
from apps.authentication.models import *
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Create superuser"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        """ """
        
        user = CustomUser.objects.create_superuser(
            os.getenv("DJANGO_SUPERUSER_USERNAME"),
            os.getenv("DJANGO_SUPERUSER_EMAIL"),
            os.getenv("DJANGO_SUPERUSER_PASSWORD"))
            
        user.save()