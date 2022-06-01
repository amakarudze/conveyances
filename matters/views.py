from rest_framework import mixins, views, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Bank, ConveyanceMatter
from .serializers import BankSerializer, ConveyanceMatterSerializer, MatterSerializer
from .stages import create_conveyance_object, matters


class BankViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    permission_classes = (IsAuthenticated,)
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class ConveyanceMatterViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = ConveyanceMatter.objects.all()
    serializer_class = ConveyanceMatterSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        conveyance_matters = []
        selected_matters = self.request.matters
        for matter in selected_matters:
            for key, val in matters.items():
                if val == matter.name:
                    stages = matters[val].stages
                    conveyance_matter = create_conveyance_object(matter.name)

        serializer.save(created_by=self.request.user, matters=conveyance_matters)


class MatterView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        conveyance_matters = []
        for key in matters.keys():
            conveyance_matter = create_conveyance_object(
                matters[key]["name"], matters[key]["stages"]
            )
            conveyance_matters.append(conveyance_matter)
        results = MatterSerializer(conveyance_matters, many=True).data
        return Response(results)
