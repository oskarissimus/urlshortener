from rest_framework import generics

from .models import ShortenedURL
from .serializers import ShortenedURLSerializer


class CreateShortenedURLView(generics.CreateAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer


class RetrieveOriginalURLView(generics.RetrieveAPIView):
    lookup_field = "short_url_code"
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer
