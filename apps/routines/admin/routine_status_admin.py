from django.contrib import admin
from ..models import RoutineStatus, RoutineStatusLang

class RoutineStatusLangAdmin(admin.TabularInline):
    model = RoutineStatusLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class RoutineStatusAdmin(admin.ModelAdmin):
    inlines = [
        RoutineStatusLangAdmin,
    ]


admin.site.register(RoutineStatus, RoutineStatusAdmin)