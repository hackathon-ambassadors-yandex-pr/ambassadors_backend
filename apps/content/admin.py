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
        "incorrect_first_name",
        "incorrect_last_name",
        "incorrect_telegram_link",
        "link",
        "guide_check",
        "status",
        "uploaded_at",
        "user_comment",
        "social_network",
    )
    readonly_fields = ("uploaded_at",)


@admin.register(ContentFile)
class ContentFileAdmin(admin.ModelAdmin):
    list_display = ("id", "file")
