from django.urls import include, path

urlpatterns = [
    path("ambassadors/", include("apps.api.v1.ambassadors.urls")),
    path("tokens/", include("apps.api.v1.tokens.urls")),
    path("users/", include("apps.api.v1.users.urls")),
    path("sendings/", include("apps.api.v1.sendings.urls")),
    path("yandex_forms/", include("apps.api.v1.yandex_forms.urls")),
]
