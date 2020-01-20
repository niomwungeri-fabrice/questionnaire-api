
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls), name='questions'),
    path('questions/<str:id>/upvote', views.UpVoteQuestionView.as_view(),
         name='up-vote-question'),
    path('questions/<str:id>/downvote', views.DownVoteQuestionView.as_view(),
         name='down-vote-question')
]
