from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email_id']
    search_fields = ['username']

admin.site.register(User, UserAdmin)