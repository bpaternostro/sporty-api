from django.contrib import admin
from django.utils.html import format_html
from ..models import Goal, GoalLang

class GoalLangAdmin(admin.TabularInline):
    model = GoalLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name} - {self.exercises}"
    

class GoalAdmin(admin.ModelAdmin):
    inlines = [
        GoalLangAdmin,
    ]


admin.site.register(Goal, GoalAdmin)