from django.contrib import admin
from ..models import ExerciseStatus, ExerciseStatusLang

class ExerciseStatusLangAdmin(admin.TabularInline):
    model = ExerciseStatusLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class ExerciseStatusAdmin(admin.ModelAdmin):
    inlines = [
        ExerciseStatusLangAdmin,
    ]


admin.site.register(ExerciseStatus, ExerciseStatusAdmin)