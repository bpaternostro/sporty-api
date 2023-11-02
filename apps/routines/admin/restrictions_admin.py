from django.contrib import admin
from ..models import Restriction, RestrictionLang

class RestrictionLangAdmin(admin.TabularInline):
    model = RestrictionLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class RestrictionAdmin(admin.ModelAdmin):
    inlines = [
        RestrictionLangAdmin,
    ]


admin.site.register(Restriction, RestrictionAdmin)