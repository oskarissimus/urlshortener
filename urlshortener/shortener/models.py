import random
import string

from django.db import models


def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = "".join(random.choice(characters) for i in range(6))
    return short_url


class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True, default=generate_short_url)
