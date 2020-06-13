from django.contrib.auth.hashers import make_password
from rest_framework import serializers, exceptions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_tracking.mixins import LoggingMixin

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


class CustomerViewSet(ModelViewSet, LoggingMixin):
    serializer_class = CustomerSerializer
    authentication_classes = []

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Customer.objects.exclude(id=self.request.user.id)
        return Customer.objects.filter(is_superuser=False)

    @action(detail=False, methods=['post'], url_path='deposit', authentication_classes=[TokenAuthentication])
    def deposit(self, request, pk=None):
        auth = TokenAuthentication()
        if not auth.authenticate(request):
            raise exceptions.NotAuthenticated({'auth_token': "Auth error."})
        customer = request.user
        amount = request.data.get('amount')
        try:
            amount = float(amount)
        except ValueError:
            raise exceptions.ValidationError({'amount': "This has to be a number."})

        if float(amount) > 0.0:
            customer.balance += amount
            customer.save()
        else:
            raise exceptions.ValidationError({'amount': "This value must be greater than 0."})

        return Response({'balance': customer.balance}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='info', authentication_classes=[TokenAuthentication])
    def info(self, request, pk=None):
        auth = TokenAuthentication()
        if not auth.authenticate(request):
            raise exceptions.NotAuthenticated({'auth_token': "Auth error."})
        current_customer = request.user
        if not current_customer.is_authenticated:
            raise exceptions.NotAuthenticated("Please provide auth token.")

        return Response(CustomerSerializer(current_customer).data, status=status.HTTP_200_OK)
