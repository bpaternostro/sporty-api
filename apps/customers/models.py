from django.db import models

from ..main.models import SportyBaseModel, SportyBaseRelationsModel, SportyBaseRelationsLangModel

class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True



class CustomerStatus(SportyBaseModel):
    class Meta:
        verbose_name = "Customer status"
        verbose_name_plural = "Customer status"
    lang = models.ManyToManyField("main.Language", through="CustomerStatusLang", blank=True)


class CustomerType(SportyBaseModel):
    lang = models.ManyToManyField("main.Language", through="CustomerTypeLang", blank=True)


# Create your models here.
class Customer(SportyBaseModel):
    username = models.CharField(max_length=200) 
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    contact_type = models.ForeignKey("routines.ContactType", on_delete=models.DO_NOTHING, default=1)
    status = models.ForeignKey(CustomerStatus, on_delete=models.DO_NOTHING, default=1)
    customer_type = models.ForeignKey(CustomerType, on_delete=models.DO_NOTHING, default=1)
    routines = models.ManyToManyField('routines.Routine', through='routines.RoutineCustomers', blank=True)
    goals = models.ManyToManyField("routines.Goal", blank=True)
    level = models.ForeignKey("routines.Level", on_delete=models.DO_NOTHING, default=1)
    restrictions = models.ManyToManyField("routines.Restriction", blank=True)
    trainings_preferences = models.ManyToManyField("routines.Training", blank=True)
    lang = models.ForeignKey("main.Language", on_delete=models.DO_NOTHING, default=1)
    

class CustomerStatusLang(SportyBaseRelationsLangModel):
    customer_status = models.ForeignKey(CustomerStatus, on_delete=models.DO_NOTHING)


class CustomerTypeLang(SportyBaseRelationsLangModel):
    customer_type = models.ForeignKey(CustomerType, on_delete=models.DO_NOTHING, default=0)
