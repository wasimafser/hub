from django.db import models

# Create your models here.


class ProjectState(models.Model):
    """
    Defines states for a project.

    name: name of the state.
    order: step-up order of the state.
    description: description of the state.
    """
    name = models.CharField(max_length=200)
    order = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class ProjectType(models.Model):
    """
    Defines types for a project.

    name: name of the type.
    order: step-up order of the type.
    description: description of the type.
    """
    name = models.CharField(max_length=200)
    order = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    """
    Contains details about a project.

    name: name of the project.
    description: description of the project.
    extras: extra information about the project.
    type: type of the project.
    state: state of the project.
    """
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    extras = models.JSONField(default=dict)
    type = models.ForeignKey(ProjectType, on_delete=models.PROTECT, null=True)
    state = models.ForeignKey(ProjectState, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name
