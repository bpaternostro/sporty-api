from django.contrib import admin
from ..models import Language, LanguageLang

class LanguageLangAdmin(admin.TabularInline):
    model = LanguageLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class LanguageAdmin(admin.ModelAdmin):
    inlines = [
        LanguageLangAdmin,
    ]


admin.site.register(Language, LanguageAdmin)