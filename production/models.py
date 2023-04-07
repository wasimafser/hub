from django.db import models

# Create your models here.


class Project(models.Model):
    """
    Contains details about a project.
    """
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    extras = models.JSONField(default=dict)

    def __str__(self) -> str:
        return self.name
