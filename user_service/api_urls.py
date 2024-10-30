from django.urls import path
from .views import UserDetailAPI

urlpatterns = [
    path('user/<int:pk>/', UserDetailAPI.as_view(), name='user_detail_api'),
]
