from django.urls import path, include
from rest_framework.routers import DefaultRouter

from plans.api.v1.viewsets import PlanViewSet

router = DefaultRouter()
router.register("plans", PlanViewSet, basename="plan")

urlpatterns = [
    path("/", include(router.urls)),
]