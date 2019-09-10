from .models import Tag, MeetUp
from .serializers import TagSerializer, MeetUpSerializer
from rest_framework import viewsets


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class MeetUpViewSet(viewsets.ModelViewSet):
    queryset = MeetUp.objects.all()
    serializer_class = MeetUpSerializer
