from django.urls import path, include
from rest_framework.routers import DefaultRouter

from servicearea.views import AddServiceAreaView, ServiceAreaViewSet, query

router = DefaultRouter()
router.register(r'area', ServiceAreaViewSet, basename='service')


urlpatterns = [
    path('', AddServiceAreaView.as_view(), name='service_area_view'),
    path('', include(router.urls)),
    path('query', query),
]
