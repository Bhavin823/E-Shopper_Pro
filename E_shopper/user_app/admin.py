from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact')

admin.site.register(UserProfile, UserProfileAdmin)