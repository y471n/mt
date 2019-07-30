from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('providers', views.ProviderView)
router.register('languages', views.LanguageView)
router.register('currencies', views.CurrencyView)

urlpatterns = [
    path('', include(router.urls))
    # path('', views.ProviderList.as_view(), name='provider_list'),
    # path('view/<uuid:pk>', views.ProviderDetail.as_view(), name='provider_view'),
    # path('new', views.ProviderCreate.as_view(), name='provider_create'),
    # path('edit/<int:pk>', views.ProviderUpdate.as_view(), name='book_edit'),
    # path('delete/<int:pk>', views.ProviderDelete.as_view(), name='book_delete'),

]
