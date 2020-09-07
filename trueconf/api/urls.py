from django.urls import path
from .views import (
   UserCreateView,
)


urlpatterns = [
    path('user/create/', UserCreateView.as_view(), name='create-user'),
    # path('users/', create, name='users'),
    # path('user/<int:pk>/', create, name='user-detail'),
    # path('user/delete/<int:pk>/', create, name='delete-user'),
    # path('user/update/<int:pk>/', create, name='update-user'),

]
