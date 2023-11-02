from django.contrib import admin
from ..models import MuscleGroupType, MuscleGroupTypeLang


class MuscleGroupTypeLangAdmin(admin.TabularInline):
    model = MuscleGroupTypeLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class MuscleGroupTypeAdmin(admin.ModelAdmin):
    inlines = [
        MuscleGroupTypeLangAdmin,
    ]


admin.site.register(MuscleGroupType, MuscleGroupTypeAdmin)