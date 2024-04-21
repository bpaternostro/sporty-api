from django.contrib import admin
from django.utils.html import format_html
from django.db.models.functions import Lower
from django.forms import Select
from django.db import models
from ..models import RoutineDaysBlocks, Routine, RoutineTargetMetaData


class RoutineMetaDataAdmin(admin.TabularInline):
    model = RoutineTargetMetaData
    list_display = ["min_age", "max_age", "goals", "level", "customer_with_equipement", "customer_train_at_home", "customer_with_lack_space", "customer_with_lack_time"]
    extra = 1

class RoutineDaysBlocksAdmin(admin.TabularInline):
    model = RoutineDaysBlocks
    list_display = ["day", "get_blocks"]
    list_filter = ["routine"]
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name} - {self.exercises}"
    
    def get_exercises(self, obj):
        blocks = obj.blocks.all()
        return "\n".join(['%s<br>' % "a" for b in blocks])
    
    def get_blocks(self, obj):
        return format_html("\n".join(['%s<br>' % b.name for b in obj.blocks.all()]))
    
    get_blocks.short_description = 'Blocks'
    get_exercises.short_description = 'Exercises'
    get_blocks.help_text = 'Authors birthday'

    #def get_ordering(self, request):
    #    return [Lower('day')]  # sort case insensitive


class RoutineAdmin(admin.ModelAdmin):
    list_display = ["name", "get_days", "description", "status", "creator"]
    inlines = [
        RoutineDaysBlocksAdmin,
        RoutineMetaDataAdmin
    ]
    
    def get_days(self, obj):
        return format_html("\n".join(['%s<br>' % d.name for d in obj.days_of_week.all()]))
    
    get_days.short_description = 'Days'


admin.site.register(Routine, RoutineAdmin)