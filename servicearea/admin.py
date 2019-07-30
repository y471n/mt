
from django.contrib.gis import admin

from servicearea.models import ServiceArea


@admin.register(ServiceArea)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'provider', 'name', 'price', 'polygon')