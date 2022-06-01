from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views

app_name = "matters"

router = DefaultRouter()
router.register("conveyance_matters", views.ConveyanceMatterViewSet)
router.register("banks", views.BankViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("matters/", views.MatterView.as_view(), name="matters"),
]
