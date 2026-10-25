from django.urls import include, url

from . import views

from rest_framework.routers import DefaultRouter
from django.conf import settings

urlpatterns = [
    url(r'^dashboard_num', views.dashboard_num),
]