from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_of_birth')




# admin.site.register(models.User, CustomUserAdmin)


# class CustomUserAdmin(UserAdmin):
#     pass
