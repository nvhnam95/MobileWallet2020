from django.contrib.auth.hashers import make_password
from rest_framework import serializers, exceptions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from MobileWallet2020.models import Customer, SavingAccount


class SavingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'balance', 'interest', 'created_time', 'saving_type']
        model = SavingAccount

    def create(self, validated_data):
        customer = self.context.get('request').user
        validated_data['customer'] = customer

        customer.balance -= validated_data.get('balance')
        customer.save()

        return super().create(validated_data)

    def validate_amount(self, amount):
        customer = self.context.get('request').user
        if customer.balance < amount:
            msg = "Error: insufficient balance."
            raise exceptions.ValidationError(msg)
        return amount


class SavingAccountViewSet(ModelViewSet):
    serializer_class = SavingAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        customer = self.request.user
        return SavingAccount.objects.filter(customer=customer)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = request.user
        saving_account = self.get_queryset().get(pk=pk)
        customer.balance += saving_account.balance
        customer.balance += saving_account.interest
        customer.save()
        return super().destroy(request, *args, **kwargs)
