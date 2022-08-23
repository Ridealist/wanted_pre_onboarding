import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model

from recruit.announce.models import Company, Announcement


User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Sequence(lambda n: "company%d" % n)
    country = "Korea"
    region = "Seoul"


class AnnounceFactory(DjangoModelFactory):
    class Meta:
        model = Announcement

    company = factory.SubFactory(CompanyFactory)
    position = factory.Sequence(lambda n: "position%d" % n)
    technology = factory.Sequence(lambda n: "tech%d" % n)
    credit = 10000
    description = "Come to join us."
