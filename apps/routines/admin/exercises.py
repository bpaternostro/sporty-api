from django.contrib import admin
from django.utils.html import format_html
from ..models import Exercise, ExerciseLang


class ExerciseLangAdmin(admin.TabularInline):
    model = ExerciseLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ["name","description","get_muscle_group", "status","creator","level", "video_link"]

    def get_muscle_group(self, obj):
        return format_html("\n".join(['%s<br>' % m.name for m in obj.muscle_group.all()]))
    
    get_muscle_group.short_description = 'Muscle_group'

    inlines = [
        ExerciseLangAdmin,
    ]

admin.site.register(Exercise, ExerciseAdmin)