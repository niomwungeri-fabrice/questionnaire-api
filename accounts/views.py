from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

User = get_user_model()


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class CreateAccountView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
