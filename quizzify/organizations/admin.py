from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from .models import (
    Organization
)

@admin.register(Organization)
class Organization(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("id", "name")}),
        # (_("Personal info"), {"fields": ("name", "email")}),
    )
    list_display = ["name"]
    search_fields = ["name"]
    readonly_fields = ['id']
