from rest_framework import serializers

from .models import Bank, ConveyanceMatter, Matter


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ("id", "name")
        read_only_fields = ("id",)


class ConveyanceMatterSerializer(serializers.ModelSerializer):
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
            "complete",
            "comment",
        )
        read_only_fields = ("id", "created_at", "last_updated")


class BaseMatterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    stages = serializers.DictField()


class MatterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matter
        fields = ("id", "name", "stages", "created_at", "last_updated")
        read_only_fields = ("created_at", "created_by", "last_updated")
