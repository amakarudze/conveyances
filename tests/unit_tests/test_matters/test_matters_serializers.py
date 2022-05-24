import pytest

from matters.serializers import BankSerializer, ConveyanceMatterSerializer
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
def test_serialize_conveyance_matter(user, bank, transfer_object, mortgage_bond_object):
    t = ConveyanceMatterFactory.build()
    valid_serialized_data = {
        "user": user.pk,
        "title": t.title,
        "matters": str([transfer_object, mortgage_bond_object]),
        "bank": bank.pk,
    }
    serializer = ConveyanceMatterSerializer(data=valid_serialized_data)

    assert serializer.is_valid(raise_exception=True)
    assert serializer.errors == {}
