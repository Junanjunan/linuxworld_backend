from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("signup/", views.SignUpView.as_view()),
    path("profile/<int:pk>/", views.ProfileView.as_view()),
    path("login", views.LogInView.as_view()),
    path("logout", views.LogOutView.as_view())
]