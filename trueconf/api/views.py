from .models import User
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView
)

from .serializers import UserCreateSerializer, UserSerializer
from rest_framework.pagination import PageNumberPagination


class Paginator(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 10


class UserCreateView(CreateAPIView):
    """Создание пользователя"""
    serializer_class = UserCreateSerializer
    http_method_names = ['post']


class UserListView(ListAPIView):
    """Возвращает список пользователей"""
    serializer_class = UserSerializer
    http_method_names = ['get']
    queryset = User.objects.all()
    pagination_class = Paginator


class UserDetailView(RetrieveAPIView):
    """Возвращает информацию о конкретном пользователе"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(RetrieveDestroyAPIView):
    """Удаление заданного пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(RetrieveUpdateAPIView):
    """Редактирование заданного пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
