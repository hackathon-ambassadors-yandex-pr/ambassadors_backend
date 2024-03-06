from django.urls import include, path

urlpatterns = [
    path("ambassadors/", include("apps.api.v1.ambassadors.urls")),
    path("tokens/", include("apps.api.v1.tokens.urls")),
    path("users/", include("apps.api.v1.users.urls")),
]
