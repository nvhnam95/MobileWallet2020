from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from MobileWallet2020.constants import MIN_TRANSFER_AMOUNT


class Customer(AbstractUser):
    balance = models.FloatField(default=0, validators=[MinValueValidator(0)])
    pass


class Transaction(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='receiver')
    amount = models.FloatField(validators=[MinValueValidator(MIN_TRANSFER_AMOUNT)])
    created_time = models.DateTimeField(auto_now=True)


class Report(models.Model):
    action = models.TextField()
    description = models.TextField(default='')
    created_time = models.DateTimeField(auto_now_add=True)


class SavingAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    saving_type = models.TextField()
    interest = models.FloatField(default=0)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

