from django.contrib import admin


from urllib import parse
from django.conf import settings
from django.utils.html import format_html
from django.db.models.functions import Lower
from django.forms import TextInput, Textarea, Select
from django.db import models
from django.shortcuts import redirect

from rest_framework.reverse import reverse

from ...main.constants import RoutineCustomerStatusChoices
from ...routines.models import RoutineCustomers, RoutineCustomerStatus, RoutineStatus
from ..models import Customer

class CustomerRoutineAdmin(admin.TabularInline):
    model = RoutineCustomers
    fields = ("routine","start_date", "due_date","status","observation")
    formfield_overrides = {
        models.CharField: {'widget': Select(attrs={'size':'10'})},
        models.CharField: {'widget': TextInput(attrs={'size':'4'})},
        models.TextField: {'widget': Textarea(attrs={'rows':5, 'cols':25})},
    }
    extra=1
    

class CustomerAdmin(admin.ModelAdmin):
    date_hierarchy = "created_on"
    #list_display = ["get_full_name", "email", "phone", "contact_type","status"]
    list_display = ["get_full_name", "email", "phone","status"]

    inlines = [
        CustomerRoutineAdmin,
    ]
    
    list_filter = [
         "customer_type",
         "status", 
    ]
    
    search_fields = (
        "get_full_name",
    )
    
    actions = ["export_routine", "send_routine"]

    # Register your models here.
    @admin.action(description="Export routine")
    def export_routine(modeladmin, request, queryset):
        routine_customer_status = RoutineCustomerStatus.objects.filter(name=RoutineCustomerStatusChoices.IN_PROGRESS).order_by('created_on').get()
        routine_customer = RoutineCustomers.objects.filter(customer=queryset.get().id, status=routine_customer_status).order_by('created_on').get()
        url = parse.urljoin(settings.SITE_URL, reverse('api:routines-export', kwargs={'pk':routine_customer.id, 'lang':routine_customer.customer.lang.code}))
        return redirect(url)

    # Register your models here.
    @admin.action(description="Send routine")
    def send_routine(modeladmin, request, queryset):
        routine_customer_status = RoutineCustomerStatus.objects.filter(name=RoutineCustomerStatusChoices.IN_PROGRESS).order_by('created_on').get()
        routine_customer = queryset.get().routines.all().filter(customer=queryset.get().id, status=routine_customer_status).get()
        #url = reverse('api:analytics-employees-confirm-import', kwargs=dict(last_import_task_id=import_id))
        

    def get_full_name(self, obj):
        return f"{obj.name} {obj.surname}"
    
    get_full_name.short_description = 'Name'

admin.site.register(Customer, CustomerAdmin)