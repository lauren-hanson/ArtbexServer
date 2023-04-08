from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from artbexapi.views import ArtBexView, FormatView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'artbexs', ArtBexView, 'artbex')
router.register(r'formats', FormatView, 'format')

urlpatterns = [
    path('', include(router.urls))
]