# Generated by Django 2.2.5 on 2019-09-12 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MeetUp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('image_url', models.ImageField(null=True, upload_to='')),
                ('tags', models.ManyToManyField(related_name='tags', to='meetups.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meet_ups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
