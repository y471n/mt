from rest_framework import serializers

from .models import Provider, Language, Currency


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ['url', 'id', 'first_name', 'last_name', 'email', 'phone_number', 'language', 'currency', ]


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['url', 'name', ]


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ['url', 'code', ]
