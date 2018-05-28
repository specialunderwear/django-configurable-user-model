from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ConfigurableUser


class ConfigurableUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Shit I just made up', {'fields': getattr(ConfigurableUser, 'extra_fields_set', [])}),
    )


admin.site.register(ConfigurableUser, ConfigurableUserAdmin)
