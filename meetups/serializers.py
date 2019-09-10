from rest_framework import serializers

from .models import Tag, MeetUp


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'url', 'name']


class MeetUpSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True,
                                              queryset=Tag.objects.all())

    class Meta:
        model = MeetUp
        fields = ['id', 'url', 'name', 'location', 'user', 'image_url',
                  'tags']
