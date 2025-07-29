from django.urls import path, include

urlpatterns = [
    path("v1/auth/", include("accounts.urls")),
]
