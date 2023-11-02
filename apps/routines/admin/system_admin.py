from django.contrib import admin
from ..models import System, SystemLang


class SystemLangAdmin(admin.TabularInline):
    model = SystemLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class SystemAdmin(admin.ModelAdmin):
    inlines = [
        SystemLangAdmin,
    ]


admin.site.register(System, SystemAdmin)