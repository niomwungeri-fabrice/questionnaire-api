from django.db import models
import uuid
from django.utils.translation import ugettext as _
from model_utils import Choices
from accounts.models import User
from meetups.models import MeetUp

TYPES = Choices(
    ('UP_VOTE', _('UpVote')),
    ('DOWN_VOTE', _('DownVote')),
)


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()
    meet_up = models.ForeignKey(MeetUp, on_delete=models.CASCADE,
                                related_name='questions')
    votes = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='questions')

    def __str__(self):
        return self.body


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField(max_length=300)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments')

    def __str__(self):
        return self.body
