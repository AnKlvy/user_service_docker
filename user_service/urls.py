from django.urls import path, include
from .views import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/new/', UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/edit/', UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('api/', include('user_service.api_urls')),  # Замените на правильное имя вашего приложения

]
