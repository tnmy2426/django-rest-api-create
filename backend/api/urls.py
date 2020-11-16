from django.contrib import admin
from django.urls import path, include
from .views import MovieViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('movie', MovieViewSet)

urlpatterns = router.urls