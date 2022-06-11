from rest_framework import mixins, views, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bank, ConveyanceMatter, Matter
from .serializers import (
    BankSerializer,
    ConveyanceMatterSerializer,
    BaseMatterSerializer,
    MatterSerializer,
    UserSerializer,
)
from .stages import create_conveyance_object, matters


class BankViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    permission_classes = (IsAuthenticated,)
    queryset = Bank.objects.all().order_by("id")
    serializer_class = BankSerializer
    lookup_field = "uuid"

    def get_queryset(self):
        name = self.request.query_params.get("name")
        queryset = self.queryset

        if name:
            return queryset.filter(name__icontains=name).order_by("id")
        return queryset


class ConveyanceMatterViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = ConveyanceMatter.objects.all().order_by("-created_at")
    serializer_class = ConveyanceMatterSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "uuid"

    def get_queryset(self):
        bank = self.request.query_params.get("bank")
        title = self.request.query_params.get("title")
        queryset = self.queryset

        if bank:
            return queryset.filter(bank__name__icontains=bank).order_by("-created_at")
        if title:
            return queryset.filter(title__icontains=title).order_by("-created_at")
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class BaseMatterView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        conveyance_matters = []
        for key in matters.keys():
            conveyance_matter = create_conveyance_object(
                matters[key]["name"], matters[key]["stages"]
            )
            conveyance_matters.append(conveyance_matter)
        results = BaseMatterSerializer(conveyance_matters, many=True).data
        return Response(results)


class MatterViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Matter.objects.all().order_by("-id")
    permission_classes = (IsAuthenticated,)
    serializer_class = MatterSerializer
    lookup_field = "uuid"


class CurrentUserView(APIView):
    def get(self, request, format=None):
        current_user = self.request.user
        results = UserSerializer(current_user).data
        return Response(results)
