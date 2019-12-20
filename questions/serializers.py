from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = UserSerializer(partial=True, required=False)

    class Meta:
        model = Question
        fields = ['id', 'url', 'body', 'user', 'comments']
