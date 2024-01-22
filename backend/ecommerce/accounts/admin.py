from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("first_name", "surname", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("User data", {"fields": ("first_name", "surname", "address")}),
        ("Permissions", {"fields": ("is_staff",)}),
    )
