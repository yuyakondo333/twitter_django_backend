from django.urls import path, include

urlpatterns = [
    path("v1/auth/", include("accounts.urls")),
    path('v1/accounts/', include('allauth.urls')),
]
