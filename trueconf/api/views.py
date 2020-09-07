from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserCreateSerializer


class UserCreateView(APIView):
    serializer_class = UserCreateSerializer
    http_method_names = ['post']

    def post(self, request):
        serializer = UserCreateSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):

            serializer.save()
        return Response({'ok': 200})
