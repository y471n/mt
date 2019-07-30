import json
import os

from django.db import migrations

from MT.settings import BASE_DIR
from suppliers.models import Language, Currency

LANGUAGE_FILE_NAME = 'language_codes.json'
CURRENCY_FILE_NAME = 'currency_codes.json'


def load_language_data():
    language_file_absolute_path = os.path.join(BASE_DIR, 'seed', LANGUAGE_FILE_NAME)
    with open(language_file_absolute_path, "r") as f:
        data = json.load(f)
        for obj in data:
            if obj.get("English"):
                lang = Language()
                lang.name = obj.get("English")
                lang.save()


def load_currency_data():
    currency_file_absolute_path = os.path.join(BASE_DIR, 'seed', CURRENCY_FILE_NAME)
    with open(currency_file_absolute_path, "r") as f:
        data = json.load(f)
        for obj in data:
            if obj.get("AlphabeticCode"):
                currency = Currency()
                currency.code = obj.get("AlphabeticCode")
                currency.save()


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        # load_language_data(),
        # load_currency_data(),
    ]
