"""Настройки админ сайта для приложения Sendings."""

from django.contrib import admin

from apps.sendings.models import Merch, Sending


@admin.register(Merch)
class MerchAdmin(admin.ModelAdmin):
    """Настройки админ сайта для таблицы Merch."""

    list_display = ("id", "name", "type", "unit_price")
    search_fields = ("name",)
    list_filter = ("type",)


class SendingMerchInline(admin.TabularInline):
    """Виджет поля merches на странице создания объекта Sending."""

    model = Sending.merches.through
    readonly_fields = ("unit_price",)
    min_num = 1
    extra = 5


@admin.register(Sending)
class SendingAdmin(admin.ModelAdmin):
    """Настройки админ сайта для таблицы Sending."""

    list_display = ("id", "created_at", "status")
    list_filter = ("status",)
    readonly_fields = ("created_at",)
    inlines = (SendingMerchInline,)
