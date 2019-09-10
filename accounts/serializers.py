from rest_framework import serializers
from .models import User


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'url', 'email', 'first_name', 'last_name', 'is_staff',
            'is_active',)
