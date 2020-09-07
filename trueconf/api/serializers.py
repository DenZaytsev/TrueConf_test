from rest_framework import serializers

from django.conf import settings
from .json_db import JsonDB


class UserCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(max_length=100, required=False)

    def save(self, **kwargs):
        db = JsonDB(str(settings.BASE_DIR) + 'db.json')
        id = db.get_max_id()
        db.set(id, self.data)


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(max_length=100, required=False)
