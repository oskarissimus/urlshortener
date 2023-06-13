from rest_framework import serializers

from .models import ShortenedURL


class ShortenedURLSerializer(serializers.ModelSerializer):
    short_url_code = serializers.SerializerMethodField()

    class Meta:
        model = ShortenedURL
        fields = ["original_url", "short_url_code"]

    def get_short_url_code(self, instance):
        return instance.short_url_code
