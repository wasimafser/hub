from production import models

from rest_framework import serializers


class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = '__all__'
        depth = 1
