from production import models
from production import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ProjectListView(generics.ListAPIView):
    """
    API endpoint that allows projects to be viewed.
    """
    queryset = models.Project.objects.all().order_by('created_at')
    serializer_class = serializers.ProjectListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['type', 'state', 'priority']
    ordering_fields = ['created_at', 'updated_at', 'priority__order', 'state']
    search_fields = ['name', 'extras']
