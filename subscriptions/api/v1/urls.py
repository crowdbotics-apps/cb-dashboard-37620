from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from subscriptions.api.v1 import views

urlpatterns = [
    path('', views.SubscriptionListView.as_view()),
    path('<int:pk>/', views.SubscriptionDetail.as_view()),
]

urlpatterns