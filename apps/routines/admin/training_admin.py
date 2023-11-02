from django.contrib import admin
from ..models import Training, TrainingLang

class TrainingLangAdmin(admin.TabularInline):
    model = TrainingLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class TrainingAdmin(admin.ModelAdmin):
    inlines = [
        TrainingLangAdmin,
    ]


admin.site.register(Training, TrainingAdmin)