from rest_framework import serializers
from drf_writable_nested.mixins import UniqueFieldsMixin
from drf_writable_nested.serializers import WritableNestedModelSerializer

from accounts.models import User
from .models import Bank, ConveyanceMatter, Matter


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ("uuid", "id", "name")
        read_only_fields = ("uuid", "id")


class MatterSerializer(UniqueFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Matter
        fields = ("uuid", "pk", "name", "stages", "created_at", "last_updated")
        read_only_fields = ("created_at", "uuid", "last_updated")
        extra_kwargs = {
            'id': {'read_only': False},
        }


class ConveyanceMatterSerializer(WritableNestedModelSerializer):
    created_by = serializers.StringRelatedField()
    bank = serializers.SlugRelatedField(
        queryset=Bank.objects.all(),
        read_only=False,
        slug_field='name'
     )
    matters = MatterSerializer(many=True)

    class Meta:
        model = ConveyanceMatter
        fields = (
            "uuid",
            "id",
            "title",
            "matters",
            "created_at",
            "last_updated",
            "created_by",
            "bank",
            "complete",
            "comment",
        )
        read_only_fields = ("created_at", "last_updated", "uuid", "pk") 


class BaseMatterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    stages = serializers.JSONField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        queryset = User.objects.all()
        fields = ("id", "username", "first_name", "last_name")
        read_only_fields = ("id",)
