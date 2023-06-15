import random

import base58
from django.db import models


def generate_short_url_code() -> str:
    length = 6
    min_value = 58 ** (length - 1)
    max_value = 58**length - 1
    val = random.randint(min_value, max_value)
    return base58.b58encode_int(val).decode()


class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_url_code = models.CharField(
        max_length=6, unique=True, default=generate_short_url_code
    )
