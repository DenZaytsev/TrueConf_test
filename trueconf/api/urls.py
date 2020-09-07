from django.urls import path
from .views import (
    UserCreateView,
    UserListView,
    UserDetailView,
    UserDeleteView,
    UserUpdateView
)


urlpatterns = [
    path('user/create/', UserCreateView.as_view(), name='create-user'),
    path('users/', UserListView.as_view(), name='users'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='delete-user'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='update-user'),

]
