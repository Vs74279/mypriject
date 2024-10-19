from django.contrib import admin
from myapp.models import Company,Employee

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=("name",'email','company') 
    search_fields=('name',)   
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)