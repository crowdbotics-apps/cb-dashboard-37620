from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()

router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")



urlpatterns = [
    path("", include(router.urls)),
    path("plans/", include('plans.api.v1.urls')),
    path('apps/', include('user_apps.api.v1.urls')),
    path('subscriptions/', include('subscriptions.api.v1.urls')),
]
