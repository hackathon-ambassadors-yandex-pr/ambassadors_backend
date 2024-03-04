from django.contrib import admin

from apps.content.models import (
    Content,
    ContentFile,
    SocialNetwork,
)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        "id", "link", "guide_check", "status",
        "uploaded_at", "user_comment", "social_network_id",
    )


@admin.register(ContentFile)
class ContentFileAdmin(admin.ModelAdmin):
    list_display = ("id", "file",)


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)
