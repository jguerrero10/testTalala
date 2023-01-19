from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from civiapp.models import Citation
from civiapp.serializers import CitationSerializer


class CitationView(CreateModelMixin, GenericViewSet):
    serializer_class = CitationSerializer
    queryset = Citation.objects.all()
