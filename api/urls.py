from django.urls import path, include

urlpatterns = [
    path('v1/accounts/', include('allauth.urls')),
]
