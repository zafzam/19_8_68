from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('stid', 'name_prefix', 'first_name', 'last_name')
    list_search = ('stid', 'first_name', 'last_name')
    
 

