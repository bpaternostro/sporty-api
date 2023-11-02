from django.contrib import admin
from django.utils.html import format_html
from django.db.models.functions import Lower
from django.forms import TextInput, Textarea, Select, SelectMultiple
from django.db import models

from ..models import Block, BlockExerciseDetail

# Register your models here.

class BlockExerciseDetailAdmin(admin.TabularInline):
    model = BlockExerciseDetail
    fields = ("block","exercise","serie","reps","weight","pause","observation")
    formfield_overrides = {
        models.CharField: {'widget': Select(attrs={'size':'10'})},
        models.CharField: {'widget': TextInput(attrs={'size':'4'})},
        models.TextField: {'widget': Textarea(attrs={'rows':5, 'cols':25})},
    }
    search_fields = ['exercise']

class BlockAdmin(admin.ModelAdmin):
    date_hierarchy = "created_on"
    list_display = ["name", "status", "creator"]
    inlines = [
        BlockExerciseDetailAdmin,
    ]


admin.site.register(Block, BlockAdmin)