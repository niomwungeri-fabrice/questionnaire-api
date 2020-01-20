from rest_framework import serializers

from accounts.serializers import UserSerializer
from meetups.serializers import MeetUpSerializer
from .models import Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    meet_up = MeetUpSerializer(partial=True, required=False)
    created_by = UserSerializer(partial=True, required=False)

    class Meta:
        model = Question
        fields = ['id', 'url', 'title', 'body', 'meet_up',
                  'votes', 'created_by', 'comments']
