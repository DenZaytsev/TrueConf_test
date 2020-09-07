from django.urls import path
from .views import (UserCreateView,
                    UserListView,
                    UserDetailView,
                    UserDeleteView,
                    UserUpdateView
                    )

urlpatterns = [

    path('user/create/', UserCreateView.as_view()),
    path('user/list/', UserListView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('user/delete/<int:pk>/', UserDeleteView.as_view()),
    path('user/update/<int:pk>/', UserUpdateView.as_view()),


]