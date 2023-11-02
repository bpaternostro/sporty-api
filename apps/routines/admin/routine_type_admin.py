from django.contrib import admin
from ..models import RoutineType, RoutineTypeLang

class RoutineTypeLangAdmin(admin.TabularInline):
    model = RoutineTypeLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class RoutineTypeAdmin(admin.ModelAdmin):
    inlines = [
        RoutineTypeLangAdmin,
    ]


admin.site.register(RoutineType, RoutineTypeAdmin)