from django.urls import include, path

from . import views

from rest_framework.routers import DefaultRouter
from django.conf import settings
router = DefaultRouter()
router.register(r'myprofile', views.MyProfileViewSet, basename='myprofile')
router.register(r'devholder', views.DevHolderViewSet, basename='devholder')
router.register(r'sceholder', views.ScenarioHolderViewSet, basename='sceholder')

urlpatterns = [
    path(r'^', include(router.urls)),
]