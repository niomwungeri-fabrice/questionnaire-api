import factory
from meetups.models import MeetUp
from accounts.models import User


class AccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
    email = factory.Faker('email')
    password = factory.Faker('password')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_staff = False
    is_superuser = False


class MeetUpFactory(factory.DjangoModelFactory):
    class Meta:
        model = MeetUp

    name = factory.Sequence(lambda x: "meeting%d" % x)
    location = factory.Sequence(lambda x: "location%d" % x)
    image_url = "https://factoryboy.readthedocs.io/en/latest/"
    user = factory.SubFactory(AccountFactory)
