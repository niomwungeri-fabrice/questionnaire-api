from rest_framework.response import Response

from meetups.models import MeetUp
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import viewsets, generics, status, permissions


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        meet_up = MeetUp.objects.get(id=self.request.data['meet_up_id'])
        serializer.save(created_by=user, meet_up=meet_up)


class UpVoteQuestionView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def patch(self, request, *args, **kwargs):
        question = self.get_object()
        question.votes += 1
        serializer = self.serializer_class(question, data=request.data,
                                           context={'request': request},
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class DownVoteQuestionView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def patch(self, request, *args, **kwargs):
        question = self.get_object()
        question.votes -= 1
        serializer = self.serializer_class(question, data=request.data,
                                           context={'request': request},
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
