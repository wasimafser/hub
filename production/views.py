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


class TaskListView(generics.ListAPIView):
    """
    API endpoint that allows tasks to be listed with filters and search.
    """
    queryset = models.Task.objects.all().order_by('created_at')
    serializer_class = serializers.TaskListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['project', 'status', 'priority']
    ordering_fields = ['created_at', 'updated_at', 'priority__order', 'status']
    search_fields = ['name', 'extras']
