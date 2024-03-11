from rest_framework.response import Response
from rest_framework.views import APIView

from apps.ambassadors.models import Ambassador, Program, Target
from apps.api.v1.ambassadors.serializers import (
    ProgramSerializer,
    TargetSerializer,
)
from apps.api.v1.drf_spectacular.custom_decorators import (
    get_drf_spectacular_view_decorator,
)
from apps.api.v1.reference_books.serializers import (
    AmbassadorReferenceBooksSerializer,
    MerchReferenceBooksSerializer,
    SocialNetworkReferenceBooksSerializer,
)
from apps.content.models import SocialNetwork
from apps.sendings.models import Merch


@get_drf_spectacular_view_decorator("reference_books")
class ReferenceBooksAmbassadorsView(APIView):
    """Обработчик запросов получения списка амбассадоров для выбора в новой отправке мерча."""

    def get(self, request):
        ambassadors = Ambassador.objects.all()
        serializer = AmbassadorReferenceBooksSerializer(ambassadors, many=True)
        return Response(serializer.data)


@get_drf_spectacular_view_decorator("reference_books")
class ReferenceBooksMerchView(APIView):
    """Обработчик запросов для получения справочника мерча."""

    def get(self, request):
        merch = Merch.objects.all()
        serializer = MerchReferenceBooksSerializer(merch, many=True)
        return Response(serializer.data)


@get_drf_spectacular_view_decorator("reference_books")
class ReferenceBooksProgramsView(APIView):
    """Обработчик запросов для получения справочника програм обучения для анкеты."""

    def get(self, request):
        programs = Program.objects.all()
        serializer = ProgramSerializer(programs, many=True)
        return Response(serializer.data)


@get_drf_spectacular_view_decorator("reference_books")
class ReferenceBooksSocialNetworksView(APIView):
    """Обработчик запросов для получения справочника площадок размещения контента."""

    def get(self, request):
        networks = SocialNetwork.objects.all()
        serializer = SocialNetworkReferenceBooksSerializer(networks, many=True)
        return Response(serializer.data)


@get_drf_spectacular_view_decorator("reference_books")
class ReferenceBooksTargetsView(APIView):
    """Обработчик запросов получения справочника целей амбассадорства для анкеты."""

    def get(self, request):
        targets = Target.objects.all()
        serializer = TargetSerializer(targets, many=True)
        return Response(serializer.data)
