from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from user_apps.api.v1 import views

urlpatterns = [
    path('', views.UserAppList.as_view()),
    path('<int:pk>/', views.UserAppDetail.as_view()),
]