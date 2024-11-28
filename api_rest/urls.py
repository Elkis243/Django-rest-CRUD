from django.urls import path
from .views import SchoolView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("auth/", obtain_auth_token),
    path("school/", SchoolView.as_view(), name="school"),
    path("school/<int:id>/", SchoolView.as_view(), name="school_params"),
]
