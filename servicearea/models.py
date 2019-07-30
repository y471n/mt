from django.db import models

from suppliers.models import BaseModel, Provider
from django.contrib.gis.db import models as geomodels


class ServiceArea(BaseModel):
    polygon = geomodels.PolygonField()
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=0)
