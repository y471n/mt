import uuid

from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,
                          primary_key=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Language(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{name}".format(name=self.name)


class Currency(BaseModel):
    code = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return "{code}".format(code=self.code)


class Provider(BaseModel):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{first_name} <{email}>".format(first_name=self.first_name, email=self.email)
