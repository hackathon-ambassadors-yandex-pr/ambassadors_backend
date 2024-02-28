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
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Ambassador)
class AmbassadorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "registration_date")
    search_fields = ("first_name", "last_name")
    empty_value_display = "-пусто-"


@admin.register(Target)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(AmbassadorTarget)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "ambassador", "target")


@admin.register(Promocode)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("value", "ambassador", "replaced_at", "is_current")


@admin.register(Address)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("ambassador", "country", "city", "address", "code", "is_current")
    search_fields = ("country", "city")
