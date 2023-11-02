from django.contrib import admin
from ..models import RoutineCustomerStatus, RoutineCustomerStatusLang


class RoutineCustomerStatusLangAdmin(admin.TabularInline):
    model = RoutineCustomerStatusLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class RoutineCustomerStatusAdmin(admin.ModelAdmin):
    inlines = [
        RoutineCustomerStatusLangAdmin,
    ]


admin.site.register(RoutineCustomerStatus, RoutineCustomerStatusAdmin)