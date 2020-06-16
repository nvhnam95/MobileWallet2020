from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

from MobileWallet2020.services.schedule_service import background_schedule_service
from MobileWallet2020.views.customer import CustomerViewSet
from MobileWallet2020.views.saving_account import SavingAccountViewSet
from MobileWallet2020.views.transaction import TransactionViewSet
from MobileWallet2020.vue_support import index

router = routers.SimpleRouter(trailing_slash=False)

router.register('customers', CustomerViewSet, basename='customer')
router.register('transactions', TransactionViewSet, basename='transaction')
router.register('saving-accounts', SavingAccountViewSet, basename='saving-account')

v1_api = [
    path('auth-tokens', views.obtain_auth_token),
    path('', include(router.urls))

]

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include(v1_api)),
                  path('', index, name='index'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

background_schedule_service()
