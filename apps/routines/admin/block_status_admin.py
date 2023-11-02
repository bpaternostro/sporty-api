from django.contrib import admin
from django.utils.html import format_html
from ..models import BlockStatus, BlockStatusLang

class BlockStatusLangAdmin(admin.TabularInline):
    model = BlockStatusLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class BlockStatusAdmin(admin.ModelAdmin):
    inlines = [
        BlockStatusLangAdmin,
    ]


admin.site.register(BlockStatus, BlockStatusAdmin)