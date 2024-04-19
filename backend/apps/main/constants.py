from django.db import models

class RoutineStatusChoices(models.TextChoices):
    IN_PROGRESS = 'in-progress'
    READY = 'ready'
    COMPLETED = 'completed'
    CANCELED = 'canceled'

class RoutineCustomerStatusChoices(models.TextChoices):
    IN_PROGRESS = 'in-progress'
    READY = 'ready'
    COMPLETED = 'completed'
    CANCELED = 'canceled'

class LanguagesChoices(models.TextChoices):
    ENGLISH = 'en'
    SPANISH = 'es'
    PORTUGUESE = 'pt'
    CHINESE = 'zh-cn'

class TokenStatusChoices(models.IntegerChoices):
    ACTIVE= 1, ('Active')
    EXPIRED = 2, ('Expire')

class CountryChoices(models.IntegerChoices):
    ARGENTINA= 1, ('Argentina')
    BRASIL = 2, ('Brasil')
    CHILE = 3, ('Chile')



CODE_LANGS = {
            "es":"spanish",
            "en":"english",
            "pt":"portuguese",
            "zh-cn":"chinese"
}