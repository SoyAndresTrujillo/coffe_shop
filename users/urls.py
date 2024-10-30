from django.urls import path
from .views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
