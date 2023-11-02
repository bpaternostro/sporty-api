from django.contrib import admin
from ..models import CustomerStatus, CustomerStatusLang

class CustomerStatusLangAdmin(admin.TabularInline):
    model = CustomerStatusLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class CustomerStatusAdmin(admin.ModelAdmin):
    inlines = [
        CustomerStatusLangAdmin,
    ]


admin.site.register(CustomerStatus, CustomerStatusAdmin)