from django.contrib import admin

from apps.content.models import Content, ContentFile, SocialNetwork


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ambassador",
        "first_name_from_form",
        "last_name_from_form",
        "telegram_link_from_form",
        "link",
        "guide_check",
        "status",
        "uploaded_at",
        "user_comment",
        "social_network",
    )
    readonly_fields = ("uploaded_at",)
    list_filter = ("status", "guide_check")


@admin.register(ContentFile)
class ContentFileAdmin(admin.ModelAdmin):
    list_display = ("id", "file")
