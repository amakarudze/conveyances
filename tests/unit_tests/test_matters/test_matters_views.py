import json

from django.urls import reverse

from rest_framework import status

from matters.models import Bank, ConveyanceMatter, Matter
from matters.serializers import (
    BankSerializer,
    ConveyanceMatterSerializer,
    MatterSerializer,
)


BASE_MATTERS_URL = reverse("matters:base_matters")
BANKS_URL = reverse("matters:bank-list")
CONVEYANCES_URL = reverse("matters:conveyancematter-list")
MATTERS_URL = reverse("matters:matter-list")


def bank_detail_url(bank_uuid):
    return reverse("matters:bank-detail", args=[bank_uuid])


def conveyance_matter_detail_url(conveyancematter_uuid):
    return reverse("matters:conveyancematter-detail", args=[conveyancematter_uuid])


def matter_detail_url(matter_uuid):
    return reverse("matters:matter-detail", args=[matter_uuid])


def test_base_matters_view_unauthenticated(client):
    response = client.get(BASE_MATTERS_URL)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_banks_view_unauthenticated(client):
    response = client.get(BANKS_URL)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_conveyance_matters_view_unauthenticated(client):
    response = client.get(CONVEYANCES_URL)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_matters_view_unauthenticated(client):
    response = client.get(MATTERS_URL)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_base_matters_view(user_client, conveyances):
    response = user_client.get(BASE_MATTERS_URL)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == conveyances


def test_get_banks_view(user_client, bank, bank2):
    response = user_client.get(BANKS_URL)

    banks = Bank.objects.all().order_by("id")
    serializer = BankSerializer(banks, many=True)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 2
    assert response.data["results"] == serializer.data


def test_get_conveyance_matters(user_client, conveyance_matter, conveyance_matters):
    response = user_client.get(CONVEYANCES_URL)

    matters = ConveyanceMatter.objects.all().order_by("-created_at")
    serializer = ConveyanceMatterSerializer(matters, many=True)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 2
    assert response.data["results"] == serializer.data


def test_get_matters_view(user_client, sample_matter, sample_matter2, sample_matter3):
    response = user_client.get(MATTERS_URL)

    matters = Matter.objects.all().order_by("-created_at")
    serializer = MatterSerializer(matters, many=True)

    assert response.status_code == status.HTTP_200_OK
    print(response.data)
    assert len(response.data["results"]) == 3
    assert response.data["results"] == serializer.data


def test_create_bank(user_client, bank_payload):
    payload = bank_payload
    response = user_client.post(BANKS_URL, payload)

    assert response.status_code == status.HTTP_201_CREATED
    bank = Bank.objects.get(id=response.data["id"])
    for key in payload.keys():
        assert payload[key] == getattr(bank, key)


def test_edit_bank(user_client, edit_bank, bank):
    payload = edit_bank
    url = bank_detail_url(bank.uuid)
    response = user_client.put(url, payload)
    bank.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert bank.name == payload["name"]


def test_create_convenience_matter_no_matter(user_client, conveyance_matter_payload):
    payload = conveyance_matter_payload
    response = user_client.post(CONVEYANCES_URL, payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED


def test_create_convenience_matter_one_matter(user_client, conveyance_matter_one_matter_payload):
    payload = conveyance_matter_one_matter_payload
    response = user_client.post(CONVEYANCES_URL, payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED


def test_create_convenience_matter_with_two_matters(user_client, conveyance_two_matters_payload):
    payload = conveyance_two_matters_payload
    response = user_client.post(CONVEYANCES_URL, payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED


def test_edit_conveyance_matter(
    user_client, basic_conveyance_matter, edit_conveyance_matter_payload
):
    payload = edit_conveyance_matter_payload
    url = conveyance_matter_detail_url(basic_conveyance_matter.uuid)
    response = user_client.patch(url, payload, format="json")

    assert response.status_code == status.HTTP_200_OK
    matters = basic_conveyance_matter.matters.all()
    assert len(matters) == 1


def test_create_matter(user_client, create_matter):
    payload = create_matter
    response = user_client.post(MATTERS_URL, payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED


def test_edit_matter(user_client, sample_matter2, edit_matter):
    payload = edit_matter

    url = matter_detail_url(sample_matter2.uuid)
    response = user_client.patch(url, payload, format="json")

    assert response.status_code == status.HTTP_200_OK
