from django.urls import path

from apps.api.v1.reference_books.views import (
    ReferenceBooksAmbassadorsView,
    ReferenceBooksMerchView,
    ReferenceBooksProgramsView,
    ReferenceBooksSocialNetworksView,
    ReferenceBooksTargetsView,
)

urlpatterns = [
    path(
        "ambassadors/",
        ReferenceBooksAmbassadorsView.as_view(),
        name="reference_books_ambassadors",
    ),
    path("merch/", ReferenceBooksMerchView.as_view(), name="reference_books_merch"),
    path(
        "programs/",
        ReferenceBooksProgramsView.as_view(),
        name="reference_books_programs",
    ),
    path(
        "social_networks/",
        ReferenceBooksSocialNetworksView.as_view(),
        name="reference_books_social_networks",
    ),
    path(
        "targets/", ReferenceBooksTargetsView.as_view(), name="reference_books_targets"
    ),
]
