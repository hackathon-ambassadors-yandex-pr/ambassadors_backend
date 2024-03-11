from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.api.v1.ambassadors.serializers import (
    ProgramSerializer,
    TargetSerializer,
)
from apps.api.v1.drf_spectacular.core.serializers import (
    Response401Serializer,
)
from apps.api.v1.reference_books.serializers import (
    AmbassadorReferenceBooksSerializer,
    MerchReferenceBooksSerializer,
    SocialNetworkReferenceBooksSerializer,
)

REFERENCE_BOOKS_VIEW_DECORATORS = {
    "ReferenceBooksAmbassadorsView": extend_schema_view(
        get=extend_schema(
            description="Список амбассадоров для выбора в новой отправке мерча",
            tags=("Reference Books",),
            responses={
                status.HTTP_200_OK: AmbassadorReferenceBooksSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
    "ReferenceBooksMerchView": extend_schema_view(
        get=extend_schema(
            description="Справочник мерча",
            tags=("Reference Books",),
            responses={
                status.HTTP_200_OK: MerchReferenceBooksSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
    "ReferenceBooksProgramsView": extend_schema_view(
        get=extend_schema(
            description="Справочник программ обучения для анкеты",
            tags=("Reference Books",),
            responses={
                status.HTTP_200_OK: ProgramSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
    "ReferenceBooksSocialNetworksView": extend_schema_view(
        get=extend_schema(
            description="Справочник площадок размещения контента / активностей амбассадора",
            tags=("Reference Books",),
            responses={
                status.HTTP_200_OK: SocialNetworkReferenceBooksSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
    "ReferenceBooksTargetsView": extend_schema_view(
        get=extend_schema(
            description="Справочник целей амбассадорства для анкеты",
            tags=("Reference Books",),
            responses={
                status.HTTP_200_OK: TargetSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
}
