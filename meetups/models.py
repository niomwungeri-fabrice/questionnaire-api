from django.db import models
import uuid
from accounts.models import User
from datetime import datetime
from model_utils import Choices
from django.utils.translation import ugettext as _

TYPES = Choices(
    ('APPEARANCE_OR_SIGNING', _('Appearance or Signing')),
    ('ATTRACTION', _('Attraction')),
    ('CAMP_TRIP_RETREAT', _('Camp, Trip, or Retreat')),
    ('CLASS_TRAINING_WORKSHOP', _('Class, Training, or Workshop')),
    ('CONCERT_OR_PERFORMANCE', _('Concert or Performance')),
    ('CONFERENCE', _('Conference')),
    ('CONVENTION', _('Convention')),
    ('DINNER_OR_GALA', _('Dinner or Gala')),
    ('FESTIVAL_OR_FAIR', _('Festival or Fair')),
    ('GAME_OR_COMPETITION', _('Game or Competition')),
    ('MEETING_OR_NETWORKING_EVENT', _('Meeting or Networking Event')),
    ('PARTY_OR_SOCIAL_GATHERING', _('Party or Social Gathering')),
    ('RACE_OR_ENDURANCE_EVENT', _('Race or Endurance Event')),
    ('RALLY', _('Rally')),
    ('SCREENING', _('Screening')),
    ('SEMINAR_OR_TALK', _('Seminar or Talk')),
    ('TOUR', _('Tour')),
    ('TOURNAMENT', _('Tournament')),
    ('TRADE_SHOW_CONSUMER_SHOW_OR_EXPO',
     _('TradeS how, Consumer Show, or Expo')),
    ('OTHER', _('Other')),
)


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class MeetUp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    venue = models.CharField(max_length=250)
    image_url = models.ImageField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='meet_ups')
    start_date = models.DateTimeField(datetime.now)
    end_date = models.DateTimeField(datetime.now)
    event_type = models.CharField(choices=TYPES, max_length=250)
    organizer = models.CharField(max_length=250)
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        return self.name
