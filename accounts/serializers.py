from rest_framework import serializers
from django.contrib.auth import get_user_model


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'url', 'email', 'first_name', 'last_name', 'is_staff',
            'is_active',)


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = get_user_model().objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
