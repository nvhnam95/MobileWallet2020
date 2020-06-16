from django.test import TestCase
from rest_framework.test import APIRequestFactory

from MobileWallet2020.models import Customer, SavingAccount
from MobileWallet2020.views.customer import CustomerSerializer
from MobileWallet2020.views.saving_account import SavingAccountSerializer
from MobileWallet2020.views.transaction import TransactionSerializer


class TestSavingAccountSerializer(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(username='test_customer1',
                                                password='123456',
                                                balance=1000)
        factory = APIRequestFactory()
        self.request = factory.post('transactions')
        self.request.user = self.customer

    def test_validate_balance_is_greater_then_main_account_balance(self):
        serializer = SavingAccountSerializer(data={'customer': self.customer.id,
                                                   'balance': 10000,
                                                   'saving_type': 'yearly'
                                                   })

        serializer.context["request"] = self.request

        assert serializer.is_valid() is False
        assert 'balance' in serializer.errors

    def test_validate_balance_is_too_small(self):
        serializer = SavingAccountSerializer(data={'customer': self.customer.id,
                                                   'balance': -1,
                                                   'saving_type': 'yearly'
                                                   })

        serializer.context["request"] = self.request

        assert serializer.is_valid() is False
        assert 'balance' in serializer.errors

    def test_validate_amount_is_zero(self):
        serializer = SavingAccountSerializer(data={'customer': self.customer.id,
                                                   'balance': 0,
                                                   'saving_type': 'yearly'
                                                   })

        serializer.context["request"] = self.request

        assert serializer.is_valid() is False
        assert 'balance' in serializer.errors

    def test_validate_amount_is_greater_than_balance(self):
        serializer = SavingAccountSerializer(data={'customer': self.customer.id,
                                                   'balance': 0,
                                                   'saving_type': 'yearly'
                                                   })

        serializer.context["request"] = self.request

        assert serializer.is_valid() is False
        assert 'balance' in serializer.errors
