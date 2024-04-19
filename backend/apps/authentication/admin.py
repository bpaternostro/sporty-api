from django.contrib import admin
from django.db.models.functions import Lower
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(CustomUser, UserAdmin)