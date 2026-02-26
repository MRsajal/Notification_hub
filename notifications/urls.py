from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/notifications/', views.api_notifications, name='api_notifications'),
]
