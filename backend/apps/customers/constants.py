from django.db import models


class CustomerStatusChoices(models.IntegerChoices):
    ACTIVE = 1, ('Activo')
    INACTIVE = 2, ('Inactivo')
    PAUSED = 3, ('Pausado')


class CustomerTypeChoices(models.IntegerChoices):
    COACH = 1, ('Profesor')
    CUSTOMER = 2, ('Alumno')
    ADMIN = 3, ('Admin')


class CustomerRangeAgeChoices(models.IntegerChoices):
    NO_LIMIT = 1, ('no limit')
    FROM_18_TO_30 = 2, ('18-30')
    FROM_30_TO_40 = 3, ('30-40')
    FROM_40_TO_50 = 4, ('40-50')
    FROM_50_TO_60 = 5, ('50-60')
    FROM_60_TO_70 = 6, ('60-70')