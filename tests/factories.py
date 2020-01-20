import factory
from meetups.models import MeetUp, Tag
from accounts.models import User
from questions.models import Question

test_user = {"email": "admin@email.com", "password": "Password123"}


class AccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
    email = factory.Faker('email')
    password = factory.Faker('password')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_staff = True
    is_superuser = False


class TagFactory(factory.DjangoModelFactory):
    class Meta:
        model = Tag
    name = factory.Sequence(lambda x: "tag%d" % x)


class MeetUpFactory(factory.DjangoModelFactory):
    class Meta:
        model = MeetUp

    name = factory.Sequence(lambda x: "meeting%d" % x)
    venue = factory.Sequence(lambda x: "venue%d" % x)
    event_type = "CLASS_TRAINING_WORKSHOP"
    user = factory.SubFactory(AccountFactory)


class QuestionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Question
    title = factory.Sequence(
        lambda x: "Why the meeting is so boring ?%d" % x),
    body = "It started a bit long for professionals",
    meet_up = factory.SubFactory(MeetUpFactory)
    created_by = factory.SubFactory(AccountFactory)


def sample_meet_up(user, **kwargs):
    defaults = {
        "name": "20th Tech Summit",
        "venue": "Telecom House",
        "event_type": "CLASS_TRAINING_WORKSHOP",
    }
    defaults.update(kwargs)
    return MeetUp.objects.create(user=user, **defaults)


def sample_user(email=test_user['email'], password=test_user['password']):
    user = User.objects.create_user(
        email=email, password=password,
    )
    return user


def sample_super_user(email="admin1@email.com",
                      password=test_user['password'],
                      is_superuser=True,
                      is_staff=True):
    user = User.objects.create_superuser(
        email=email,
        password=password,
        is_superuser=is_superuser,
        is_staff=is_staff
    )
    return user
