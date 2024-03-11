"""Настройки URL эндпоинтов yandex_forms/ API v1."""

from django.urls import path

from apps.api.v1.yandex_forms.views import process_ambassador_form, process_content_form

urlpatterns = [
    path("ambassador_forms/", process_ambassador_form, name="ambassador_forms"),
    path("content_forms/", process_content_form, name="content_forms"),
]
