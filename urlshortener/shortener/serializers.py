from rest_framework import serializers

from .models import ShortenedURL


class ShortenedURLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortenedURL
        fields = ["original_url", "short_url"]

    def get_short_url(self, instance):
        return instance.short_url
