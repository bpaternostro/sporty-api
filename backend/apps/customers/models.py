from django.db import models

from ..main.models import FitboxBaseModel, FitboxBaseRelationsModel, FitboxBaseRelationsLangModel
from .constants import *
from ..routines.constants import *

from ..authentication.models import CustomUser
from ..main.models import BaseModel
from ..main.constants import CountryChoices


class CustomerTest(FitboxBaseModel):
    value = models.FloatField(max_length=3, blank=True)


class Customer(BaseModel):
    customer = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    routines = models.ManyToManyField('routines.Routine', through='routines.RoutineCustomers', blank=True)
    goals = models.ManyToManyField('routines.Goal', blank=True)
    restrictions = models.ManyToManyField('routines.Restriction', blank=True)
    level = models.ForeignKey('routines.Level', on_delete=models.CASCADE,  default=LevelChoices.INITIAL)
    trainings_preferences = models.ManyToManyField('routines.Training', blank=True)
    country = models.IntegerField(choices=CountryChoices.choices, default=CountryChoices.ARGENTINA)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    weight = models.FloatField(max_length=3, blank=True, null=True)
    height = models.FloatField(max_length=3, blank=True, null=True)
    imc = models.FloatField(max_length=3, blank=True, null=True)
    customer_test_values = models.ManyToManyField(CustomerTest, blank=True)
    customer_with_equipement = models.IntegerField(choices=YesNoChoices.choices, default=YesNoChoices.NO)
    customer_train_at_home = models.IntegerField(choices=YesNoChoices.choices, default=YesNoChoices.NO)
    customer_with_lack_space = models.IntegerField(choices=YesNoChoices.choices, default=YesNoChoices.NO)
    customer_with_lack_time = models.IntegerField(choices=YesNoChoices.choices, default=YesNoChoices.NO)
