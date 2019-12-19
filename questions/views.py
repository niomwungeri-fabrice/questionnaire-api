from .models import Question
from .serializers import QuestionSerializer
from rest_framework import viewsets


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
