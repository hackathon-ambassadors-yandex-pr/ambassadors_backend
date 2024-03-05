from django.urls import include, path

urlpatterns = [
    path("tokens/", include("apps.api.v1.tokens.urls")),
    path("users/", include("apps.api.v1.users.urls")),
    path("sendings/", include("apps.api.v1.sendings.urls")),
]
