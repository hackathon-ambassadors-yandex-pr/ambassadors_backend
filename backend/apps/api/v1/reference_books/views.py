from apps.ambassadors.models import Ambassador, Program, Target
from apps.api.v1.ambassadors.serializers import (
    ProgramSerializer,
    RetrieveAmbassadorSerializer,
    TargetSerializer,
)
from apps.api.v1.reference_books.serializers import (
    MerchSerializer,
    SocialNetworkSerializer,
)
from apps.content.models import SocialNetwork
from apps.sendings.models import Merch
from rest_framework.response import Response
from rest_framework.views import APIView


class ReferenceBooksAmbassadorsView(APIView):
    """Обработчик запросов получения списка амбассадоров для выбора в новой отправке мерча."""

    def get(self, request):
        ambassadors = Ambassador.objects.all()
        serializer = RetrieveAmbassadorSerializer(ambassadors, many=True)
        return Response(serializer.data)


class ReferenceBooksMerchView(APIView):
    """Обработчик запросов для получения справочника мерча."""

    def get(self, request):
        merch = Merch.objects.all()
        serializer = MerchSerializer(merch, many=True)
        return Response(serializer.data)


class ReferenceBooksProgramsView(APIView):
    """Обработчик запросов для получения справочника програм обучения для анкеты."""

    def get(self, request):
        programs = Program.objects.all()
        serializer = ProgramSerializer(programs, many=True)
        return Response(serializer.data)


class ReferenceBooksSocialNetworksView(APIView):
    """Обработчик запросов для получения справочника площадок размещения контента."""

    def get(self, request):
        networks = SocialNetwork.objects.all()
        serializer = SocialNetworkSerializer(networks, many=True)
        return Response(serializer.data)


class ReferenceBooksTargetsView(APIView):
    """Обработчик запросов получения справочника целей амбассадорства для анкеты."""

    def get(self, request):
        targets = Target.objects.all()
        serializer = TargetSerializer(targets, many=True)
        return Response(serializer.data)
