from django.contrib import admin
from ..models import MuscleGroup, MuscleGroupLang


class MuscleGroupLangAdmin(admin.TabularInline):
    model = MuscleGroupLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class MuscleGroupAdmin(admin.ModelAdmin):
    inlines = [
        MuscleGroupLangAdmin,
    ]


admin.site.register(MuscleGroup, MuscleGroupAdmin)