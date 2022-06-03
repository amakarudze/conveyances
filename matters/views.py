from rest_framework import mixins, views, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Bank, ConveyanceMatter, Matter
from .serializers import (
    BankSerializer,
    ConveyanceMatterSerializer,
    BaseMatterSerializer,
    MatterSerializer,
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

    def get_queryset(self):
        bank = self.request.query_params.get("bank")
        title = self.request.query_params.get("title")
        queryset = self.queryset

        if bank:
            return queryset.filter(bank__icontains=bank).order_by("-created_at")
        if title:
            return queryset.filter(title__icontains=title).order_by("-created_at")
        return queryset.filter(complete=False).order_by("-created_at")

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

    def get(self, request):
        conveyance_matters = []
        for key in matters.keys():
            conveyance_matter = create_conveyance_object(
                matters[key]["name"], matters[key]["stages"]
            )
            conveyance_matters.append(conveyance_matter)
        results = BaseMatterSerializer(conveyance_matters, many=True).data

        return results, self.queryset

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)
