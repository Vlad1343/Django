
"""Define URL patterns for users."""

from django.urls import path, include

app_name = "users"
urlpatterns = [
    # Add URL authentication URLs (login, logout, password management)
    path("", include("django.contrib.auth.urls")),
]