from django.db import models
import uuid
from accounts.models import User


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class MeetUp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    image_url = models.ImageField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='meet_ups')
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        return self.name
