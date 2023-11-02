from django.contrib import admin
from ..models import Cadence, CadenceLang

class CadenceLangAdmin(admin.TabularInline):
    model = CadenceLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class CadenceAdmin(admin.ModelAdmin):
    inlines = [
        CadenceLangAdmin,
    ]


admin.site.register(Cadence, CadenceAdmin)