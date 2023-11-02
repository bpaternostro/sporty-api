from django.contrib import admin
from ..models import TrainingMethod, TrainingMethodLang


class TrainingMethodLangAdmin(admin.TabularInline):
    model = TrainingMethodLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class TrainingMethodAdmin(admin.ModelAdmin):
    inlines = [
        TrainingMethodLangAdmin,
    ]


admin.site.register(TrainingMethod, TrainingMethodAdmin)