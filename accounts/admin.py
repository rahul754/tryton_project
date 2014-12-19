from django.contrib import admin

# Register your models here.

from .moduls import  AuthProfile



class Accounts(admin.ModelAdmin): pass
admin.site.register(AuthProfile , Accounts)