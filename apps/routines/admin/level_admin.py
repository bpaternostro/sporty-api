from django.contrib import admin
from ..models import Level, LevelLang

class LevelLangAdmin(admin.TabularInline):
    model = LevelLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class LevelAdmin(admin.ModelAdmin):
    inlines = [
        LevelLangAdmin,
    ]


admin.site.register(Level, LevelAdmin)