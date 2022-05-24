import factory

from faker import Factory as FakerFactory
from pytest_factoryboy import register

from accounts.models import User


faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda x: faker.first_name())
    email = factory.LazyAttribute(lambda x: faker.email())
    password = factory.LazyAttribute(lambda x: faker.password())


register(UserFactory)
