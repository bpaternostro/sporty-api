from django.contrib import admin
from django.utils.html import format_html
from ..models import Exercise

    
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ["name","description","get_muscle_group", "status","creator","level", "video_link"]

    def get_muscle_group(self, obj):
        return format_html("\n".join(['%s<br>' % m.name for m in obj.muscle_group.all()]))
    
    get_muscle_group.short_description = 'Muscle_group'


admin.site.register(Exercise, ExerciseAdmin)