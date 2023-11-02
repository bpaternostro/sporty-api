from django.contrib import admin
from ..models import Day,DayLang

class DayLangAdmin(admin.TabularInline):
    model = DayLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name} - {self.exercises}"
    

class DayAdmin(admin.ModelAdmin):
    inlines = [
        DayLangAdmin,
    ]


admin.site.register(Day, DayAdmin)