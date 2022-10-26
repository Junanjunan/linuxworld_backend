from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("profile/<int:pk>/", views.ProfileView.as_view()),
]