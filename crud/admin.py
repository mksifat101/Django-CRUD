from django.contrib import admin
from .models import User

admin.site.register(User)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
