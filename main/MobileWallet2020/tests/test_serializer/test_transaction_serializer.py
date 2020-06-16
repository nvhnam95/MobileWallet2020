from django.test import TestCase
from rest_framework.test import APIRequestFactory

from MobileWallet2020.models import Customer
from MobileWallet2020.views.customer import CustomerSerializer
from MobileWallet2020.views.transaction import TransactionSerializer


class TestTransactionSerializer(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(username='test_customer1',
                                                  password='123456',
                                                  balance=1000)
        factory = APIRequestFactory()
        self.request = factory.post('transactions')
        self.request.user = self.customer

    def test_validate_receiver(self):
        serializer = TransactionSerializer(data={'sender': self.customer.id,
                                                 'receiver': self.customer.id,
                                                 'amount': 1})
        serializer.context["request"] = self.request

        assert serializer.is_valid() is False
        assert 'receiver' in serializer.errors

    def test_validate_amount_is_zero(self):
        serializer = TransactionSerializer(data={'sender': self.customer.id,
                                                 'receiver': self.customer.id,
                                                 'amount': 0})

        serializer.context["request"] = self.request

        assert serializer.is_valid() is False
        assert 'amount' in serializer.errors

    def test_validate_amount_is_greater_than_balance(self):
        serializer = TransactionSerializer(data={'sender': self.customer.id,
                                                 'receiver': self.customer.id,
                                                 'amount': 10000})

        serializer.context["request"] = self.request

        assert serializer.is_valid() is False
        assert 'amount' in serializer.errors

