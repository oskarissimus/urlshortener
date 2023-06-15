from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import ShortenedURL


class ShortenedURLTests(APITestCase):
    def test_create_shortened_url(self):
        """
        Ensure we can create a new shortened URL object.
        """
        url = reverse("create_shortened_url")
        data = {"original_url": "http://example.com/very-very/long/url/even-longer"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ShortenedURL.objects.count(), 1)
        self.assertEqual(
            ShortenedURL.objects.get().original_url,
            "http://example.com/very-very/long/url/even-longer",
        )

    def test_retrieve_original_url(self):
        """
        Ensure we can retrieve the original URL from a shortened URL.
        """
        # First, create a new shortened URL object.
        shortened_url = ShortenedURL.objects.create(
            original_url="http://example.com/very-very/long/url/even-longer"
        )
        # Now, retrieve it.
        url = reverse("retrieve_original_url", args=[shortened_url.short_url_code])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["original_url"],
            "http://example.com/very-very/long/url/even-longer",
        )
