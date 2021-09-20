"""N0temail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"emails", views.EmailViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("", views.index, name="index"),
    path("<str:email_name>/", views.address, name="address"),
    path("<str:email_name>/<int:email_id>/", views.email, name="email"),
    path("sendgrid", views.SendgridWebhookView, name="sendgrid"),
]
