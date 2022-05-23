from django.urls import reverse


def test_login_url(client):
    response = client.get(reverse("accounts:login"))
    assert response.status_code == 200


def test_logout_url(user_client):
    response = user_client.get(reverse("accounts:logout"))
    assert response.status_code == 302
