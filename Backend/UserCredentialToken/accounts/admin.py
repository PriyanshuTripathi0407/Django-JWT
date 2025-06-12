from django.contrib import admin
from accounts.models import *
# Register your models here.

@admin.register(UserRegistration)
class UserRegistrationModelAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','username','contact','email','address','password']
