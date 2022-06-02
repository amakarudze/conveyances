from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views

app_name = "matters"

router = DefaultRouter()
router.register("conveyance_matters", views.ConveyanceMatterViewSet)
router.register("banks", views.BankViewSet)
router.register("matters", views.MatterViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("base_matters/", views.BaseMatterView.as_view(), name="base_matters"),
]
