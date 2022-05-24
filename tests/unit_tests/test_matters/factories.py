import factory

from faker import Factory as FakerFactory
from pytest_factoryboy import register

from matters.models import Bank, ConveyanceMatter
from tests.unit_tests.test_accounts.factories import UserFactory


faker = FakerFactory.create()


class BankFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bank

    name = factory.LazyAttribute(lambda x: faker.name())


class ConveyanceMatterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ConveyanceMatter

    title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=20))
    matters = factory.LazyAttribute(lambda x: faker.sentence(nb_words=20))
    created_by = factory.SubFactory(UserFactory)
    bank = factory.SubFactory(BankFactory)


register(BankFactory)
register(ConveyanceMatterFactory)
