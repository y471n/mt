from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from suppliers.models import Provider, Language, Currency
from rest_framework import viewsets
from .serializers import ProviderSerializer, LanguageSerializer, CurrencySerializer


class ProviderView(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class CurrencyView(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


