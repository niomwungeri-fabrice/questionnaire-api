from .models import User
from .serializers import AccountSerializer
from rest_framework import viewsets


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
