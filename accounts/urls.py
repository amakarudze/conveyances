from re import template
from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import LoginForm

app_name = "accounts"


urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html",
            form_class=LoginForm,
            extra_context={"title": "Login"},
        ),
        name="login",
    ),
    path("logout/", auth_views.logout_then_login, name="logout"),
]
