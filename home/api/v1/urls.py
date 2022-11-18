from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

from plans.api.v1.viewsets import PlanViewSet

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")

router.register("plans", PlanViewSet, basename="plan")

urlpatterns = [
    path("", include(router.urls)),
]
