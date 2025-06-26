from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import (CustomUserViewSet, PaymentsCreateAPIView, PaymentsDestroyAPIView, PaymentsListAPIView,
                         PaymentsRetrieveAPIView, PaymentsUpdateAPIView)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", CustomUserViewSet, basename="users")

urlpatterns = [
                  path("payments/create/", PaymentsCreateAPIView.as_view(), name="payment_create"),
                  path("payments/", PaymentsListAPIView.as_view(), name="payments_list"),
                  path("payments/<int:pk>/", PaymentsRetrieveAPIView.as_view(), name="payment_detail"),
                  path("payments/<int:pk>/edit/", PaymentsUpdateAPIView.as_view(), name="payment_edit"),
                  path("payments/delete/<int:pk>/", PaymentsDestroyAPIView.as_view(), name="payment_delete"),
              ] + router.urls
