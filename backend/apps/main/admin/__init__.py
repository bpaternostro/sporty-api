from django.contrib import admin
from ..models import *
from .language_status_admin import *

admin.site.register(Language)