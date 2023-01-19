from django.urls import path, include
from rest_framework import routers

from civiapp.views import CitationView

router = routers.DefaultRouter()

router.register('citation', CitationView, basename='citation')

urlpatterns = [
    path('', include(router.urls))
]
