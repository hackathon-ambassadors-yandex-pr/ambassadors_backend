from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

app_name = "apps.api"

urlpatterns = [
    path("v1/", include("apps.api.v1.urls")),
    path(
        "redoc/v1/",
        TemplateView.as_view(template_name="ambassadors_v1_redoc.html"),
        name="ambassadors_v1_redoc",
    ),
    path(
        "swagger/v1/",
        TemplateView.as_view(template_name="ambassadors_v1_swagger.html"),
        name="ambassadors_v1_swagger",
    ),
]

if settings.DEBUG:
    urlpatterns += (
        path(
            "dynamic_doc/v1/download/",
            SpectacularAPIView.as_view(),
            name="schema",
        ),
        path(
            "redoc/v1/dynamic/",
            SpectacularRedocView.as_view(url_name="apps.api:schema"),
            name="redoc",
        ),
        path(
            "swagger/v1/dynamic/",
            SpectacularSwaggerView.as_view(url_name="apps.api:schema"),
            name="swagger",
        ),
    )
