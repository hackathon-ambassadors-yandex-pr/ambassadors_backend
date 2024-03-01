from django.contrib import admin

from apps.ambassadors.models import (
    Address,
    Ambassador,
    AmbassadorTarget,
    Program,
    Promocode,
    Status,
    Target,
)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Ambassador)
class AmbassadorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "registration_date")
    search_fields = ("first_name", "last_name")
    empty_value_display = "-пусто-"


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(AmbassadorTarget)
class AmbassadorTargetAdmin(admin.ModelAdmin):
    list_display = ("id", "ambassador", "target")


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ("id", "value", "ambassador", "replaced_at", "is_current")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ambassador",
        "country",
        "city",
        "address",
        "code",
        "is_current",
    )
    search_fields = ("country", "city")
