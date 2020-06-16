from django.db.models import Q
from rest_framework import serializers, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from MobileWallet2020.models import Transaction, Customer
from MobileWallet2020.services import funding_service


class TransactionSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(slug_field='username', read_only=True)
    receiver = serializers.SlugRelatedField(queryset=Customer.objects.all(),
                                            slug_field='username')

    class Meta:
        fields = ['id', 'sender', 'receiver', 'amount', 'created_time']
        model = Transaction
        read_only_fields = ['sender']

    def create(self, validated_data):
        customer = self.context.get('request').user

        validated_data['sender'] = sender = customer

        receiver = validated_data['receiver']
        amount = validated_data['amount']

        transaction = super(TransactionSerializer, self).create(validated_data)
        funding_service.make_transfer(sender, receiver, amount)

        return transaction

    def validate_receiver(self, receiver):
        customer = self.context.get('request').user
        if customer == receiver:
            msg = "Cannot send money to yourself."
            raise exceptions.ValidationError(msg)
        return receiver

    def validate_amount(self, amount):
        customer = self.context.get('request').user
        if customer.balance < amount:
            msg = "Error: insufficient balance."
            raise exceptions.ValidationError(msg)

        if amount <= 0:
            msg = "Error: amount need to be a positive number."
            raise exceptions.ValidationError(msg)

        return amount


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(Q(sender=user) | Q(receiver=user)).order_by('-created_time')
