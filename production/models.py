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


class ProjectPriority(models.Model):
    """
    Defines priorities for a project.

    name: name of the priority.
    order: step-up order of the priority.
    description: description of the priority.
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
    priority: priority of the project.
    start_date: start date of the project.
    end_date: end date of the project.
    created_at: date of creation.
    updated_at: date of last update.
    """
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    extras = models.JSONField(default=dict, null=True, blank=True)
    type = models.ForeignKey(ProjectType, on_delete=models.PROTECT, null=True)
    state = models.ForeignKey(ProjectState, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(ProjectPriority, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class TaskPriority(models.Model):
    """
    Defines priorities for a task.

    name: name of the priority.
    order: step-up order of the priority.
    description: description of the priority.
    """
    name = models.CharField(max_length=200)
    order = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class TaskStatus(models.Model):
    """
    Defines statuses for a task.

    name: name of the status.
    order: step-up order of the status.
    description: description of the status.
    """
    name = models.CharField(max_length=200)
    order = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class TaskType(models.Model):
    """
    Defines types for a task.

    name: name of the type.
    priority: prioirty multiplier of the type.
    description: description of the type.
    """
    name = models.CharField(max_length=200)
    priority = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    """
    Contains details about a task.

    title: title of the task.
    description: description of the task.
    extras: extra information about the task.
    project: project the task belongs to.
    priority: priority of the task.
    status: status of the task.
    type: type of the task.
    created_by: user who created the task.
    assigned_to: user who is assigned to the task.
    assign_date: date when the task is assigned.
    start_date: date when the task starts.
    end_date: date when the task ends.
    expected_start_date: date when the task is expected to start.
    expected_end_date: date when the task is expected to end.
    created_at: date of creation.
    updated_at: date of last update.
    extras: extra information about the task.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    priority = models.ForeignKey(TaskPriority, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(TaskType, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    assigned_to = models.ForeignKey(
        'auth.User', on_delete=models.PROTECT, related_name='assigned_to'
    )
    assign_date = models.DateTimeField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    expected_start_date = models.DateTimeField(null=True, blank=True)
    expected_end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expected_completion_duration = models.DurationField(null=True, blank=True)
    completion_duration = models.DurationField(null=True, blank=True)
    extras = models.JSONField(default=dict, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
