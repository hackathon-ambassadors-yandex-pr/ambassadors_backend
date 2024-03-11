from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Админка пользователя."""

    list_display = [
        "id",
        "first_name",
        "middle_name",
        "last_name",
        "email",
        "registration_date",
        "avatar",
    ]
    readonly_fields = ("registration_date",)
    fieldsets = (
        (None, {"fields": ("password",)}),
        (
            _("Personal info"),
            {"fields": ("last_name", "first_name", "middle_name", "email", "avatar")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "registration_date")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    ordering = ["email"]
