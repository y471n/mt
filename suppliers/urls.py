from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('providers', views.ProviderView)
router.register('languages', views.LanguageView)
router.register('currencies', views.CurrencyView)

urlpatterns = [
    path('', include(router.urls))
]
