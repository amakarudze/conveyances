import pytest

from matters.serializers import (
    BankSerializer,
    ConveyanceMatterSerializer,
    BaseMatterSerializer,
    MatterSerializer,
)
from .factories import BankFactory, ConveyanceMatterFactory


@pytest.mark.unit
def test_serialize_bank_model():
    bank = BankFactory()
    serializer = BankSerializer(bank)

    assert serializer.data


@pytest.mark.unit
def test_bank_serialized_data():
    t = BankFactory.build()
    valid_serializer_data = {"name": t.name}

    serializer = BankSerializer(data=valid_serializer_data)

    assert serializer.is_valid(raise_exception=True)
    assert serializer.errors == {}


@pytest.mark.unit
def test_serialize_conveyance_matter():
    matter = ConveyanceMatterFactory()
    serializer = ConveyanceMatterSerializer(matter)

    assert serializer.data


@pytest.mark.unit
def test_conveyance_matter_serialized_data(user, bank, sample_matter, sample_matter2):
    t = ConveyanceMatterFactory.build()
    valid_serialized_data = {
        "user": user.pk,
        "title": t.title,
        "matters": [sample_matter.pk, sample_matter2.pk],
        "bank": bank.pk,
    }
    serializer = ConveyanceMatterSerializer(data=valid_serialized_data)

    assert serializer.is_valid(raise_exception=True)
    assert serializer.errors == {}


@pytest.mark.unit
def test_serialize_matter(matter):
    serializer = MatterSerializer(matter)
    assert serializer.data


@pytest.mark.unit
def test_matter_serialized_data(user, transfer_object):
    valid_serialized_data = {
        "name": transfer_object.name,
        "created_by": user,
        "stages": transfer_object.stages,
    }

    serializer = MatterSerializer(data=valid_serialized_data)

    assert serializer.is_valid(raise_exception=True)
    assert serializer.errors == {}


@pytest.mark.unit
def test_serialize_base_matter(transfer_object):
    serializer = BaseMatterSerializer(transfer_object)
    assert serializer.data


@pytest.mark.unit
def test_base_matter_serialized_data(transfer_object):
    valid_serialized_data = {
        "name": transfer_object.name,
        "stages": transfer_object.stages,
    }

    serializer = BaseMatterSerializer(data=valid_serialized_data)

    assert serializer.is_valid(raise_exception=True)
    assert serializer.errors == {}
