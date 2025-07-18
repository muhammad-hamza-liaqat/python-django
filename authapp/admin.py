from django.contrib import admin
from authapp.models import User  # <-- import only

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'name', 'is_active', 'is_staff']

