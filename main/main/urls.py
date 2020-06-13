from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from MobileWallet2020.views.customer import CustomerViewSet
from MobileWallet2020.views.transaction import TransactionViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register('customers', CustomerViewSet)
router.register('transactions', TransactionViewSet, base_name='transaction')

v1_api = [
    path('auth-tokens', views.obtain_auth_token),
    path('', include(router.urls))

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1_api)),

]
