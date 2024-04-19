from django.db import models

class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class FitboxBaseModel(BaseModel):
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)


class FitboxBaseWithIimageModel(FitboxBaseModel):
    class Meta:
        abstract = True

    image = models.ImageField(upload_to="routines/exercises/images", blank=True)

class FitboxBaseRelationsModel(BaseModel):
    class Meta:
        abstract = True


class FitboxBaseRelationsLangModel(BaseModel):
    class Meta:
        abstract = True

    lang = models.ForeignKey("main.Language", on_delete=models.DO_NOTHING)
    translation = models.CharField(max_length=150)


class Language(FitboxBaseModel):
    code = models.CharField(blank=False, max_length=50)
    status = models.ForeignKey("main.LanguageStatus", on_delete=models.DO_NOTHING, default=1)
    encoding = models.CharField(blank=True, max_length=50)



class LanguageStatus(FitboxBaseModel):
    class Meta:
        verbose_name = "language status"
        verbose_name_plural = "Language status"
    lang = models.ManyToManyField(Language, through="LanguageStatusLang", blank=True)


class LanguageStatusLang(FitboxBaseRelationsLangModel):
    language_status = models.ForeignKey(LanguageStatus, on_delete=models.DO_NOTHING)



