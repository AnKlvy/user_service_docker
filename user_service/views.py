from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import User
from .forms import UserForm

# Список пользователей (Read - List)
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

# Детальная информация о пользователе (Read - Detail)
class UserDetailView(DetailView):
    model = User
    template_name = 'user_details.html'
    context_object_name = 'user'

# Создание нового пользователя (Create)
class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('user_list')

# Обновление пользователя (Update)
class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('user_list')

# Удаление пользователя (Delete)
class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404

class UserDetailAPI(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
