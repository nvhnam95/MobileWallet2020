import json

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, exceptions, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.hashers import make_password

from MobileWallet2020.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['username', 'password', 'balance']
        model = Customer
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'balance': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    def validate_password(self, value):
        if len(str(value)) < 6:
            msg = "Password is too short, make sure its length is more than 6."
            raise exceptions.ValidationError(msg)
        return value


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    authentication_classes = []
    queryset = Customer.objects.all()

    @action(detail=True, methods=['post'], url_path='deposit')
    def deposit(self, request, pk=None):
        try:
            customer = self.queryset.get(pk=pk)
        except Customer.DoesNotExist:
            raise exceptions.NotFound()

        amount = request.data.get('amount')
        if amount > 0:
            customer.balance += amount
            customer.save()
        else:
            raise exceptions.ValidationError({'amount': "This value must be greater than 0."})

        return Response({'balance': customer.balance}, status=status.HTTP_200_OK)
