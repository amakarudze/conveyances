from rest_framework.serializers import ModelSerializer

from .models import Bank, ConveyanceMatter


class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = ("id", "name")
        read_only_fields = ("id",)


class ConveyanceMatterSerializer(ModelSerializer):
    class Meta:
        model = ConveyanceMatter
        fields = (
            "id",
            "title",
            "matters",
            "created_at",
            "last_updated",
            "last_updated",
            "bank",
        )
        read_only_fields = ("id", "created_at", "last_updated")
