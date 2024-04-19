from django.db import models
from django.contrib.auth.models import AbstractUser   
from django.contrib.auth.models import AbstractUser

from ..main.models import BaseModel
from ..main.constants import TokenStatusChoices

from ..routines.constants import ContactTypeChoices

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    contact_type = models.IntegerField(choices=ContactTypeChoices.choices, default=ContactTypeChoices.EMAIL, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class TokenWhiteList(BaseModel):
    token = models.CharField(max_length=100, blank=True)
    status = models.IntegerField(choices=TokenStatusChoices.choices, default=TokenStatusChoices.ACTIVE)