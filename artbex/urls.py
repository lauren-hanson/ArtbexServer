from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from artbexapi.views import ArtBexView, ImageView, CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'artbexs', ArtBexView, 'artbex')
router.register(r'images', ImageView, 'image')
router.register(r'categories', CategoryView, 'category')

urlpatterns = [
    path('', include(router.urls))
]
