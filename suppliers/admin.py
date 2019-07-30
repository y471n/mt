from django.contrib import admin

from suppliers.models import Provider, Language, Currency


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'code',)


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
