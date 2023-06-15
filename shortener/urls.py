from django.urls import path

from .views import CreateShortenedURLView, RetrieveOriginalURLView

urlpatterns = [
    path("shorten/", CreateShortenedURLView.as_view(), name="create_shortened_url"),
    path(
        "<str:short_url_code>/",
        RetrieveOriginalURLView.as_view(),
        name="retrieve_original_url",
    ),
]
