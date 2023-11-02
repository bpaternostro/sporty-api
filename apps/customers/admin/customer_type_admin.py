from django.contrib import admin
from ..models import CustomerType, CustomerTypeLang

class CustomerTypeLangAdmin(admin.TabularInline):
    model = CustomerTypeLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class CustomerTypeAdmin(admin.ModelAdmin):
    inlines = [
        CustomerTypeLangAdmin,
    ]


admin.site.register(CustomerType, CustomerTypeAdmin)