from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

from .serializers import AccountSerializer, UserSerializer
from rest_framework import viewsets, generics


class AccountViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = AccountSerializer


class UserView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )