from rest_framework.views import APIView
from rest_framework.response import Response
from .json_db import JsonDB, DB_DIR
from .serializers import UserCreateSerializer, UserSerializer
import json


class UserCreateView(APIView):
    serializer_class = UserCreateSerializer
    http_method_names = ['post']

    def post(self, request):
        serializer = UserCreateSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'status': 200})


class UserListView(APIView):
    """Возвращает список пользователей"""

    def get(self, request):
        db = JsonDB(DB_DIR)
        return Response(db.db)


class UserDetailView(APIView):
    """Возвращает информацию о конкретном пользователе"""
    def get(self, request, pk):
        db = JsonDB(DB_DIR)
        user = db.get(str(pk))
        return Response(user)


class UserDeleteView(APIView):
    """Удаление заданного пользователя"""
    def delete(self, request, pk):
        db = JsonDB(DB_DIR)
        db.delete(pk)
        return Response({"status": "200"})


class UserUpdateView(APIView):
    """Редактирование заданного пользователя"""
    serializer_class = UserSerializer

    def put(self, request, pk):
        serializer = UserSerializer(data=request.data)
        db = JsonDB(DB_DIR)
        if serializer.is_valid(raise_exception=True):
            if pk in db.db:
                db.set(pk, serializer.data)
                return Response({"status": "200"})
        return Response({"status": "400"})