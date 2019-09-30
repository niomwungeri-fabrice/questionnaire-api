from rest_framework import serializers

from .models import Tag, MeetUp


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'url', 'name']


class MeetUpSerializer(serializers.ModelSerializer):
    # tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = MeetUp
        fields = ['id', 'name', 'location', 'image_url', 'user_id']
