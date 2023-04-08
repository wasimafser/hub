from django.contrib import admin

from production import models

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'state')
    search_fields = ('name', 'description')
    ordering = ('name',)
    list_filter = ('state',)


admin.site.register(models.Project, admin_class=ProjectAdmin)
admin.site.register(models.ProjectState)
admin.site.register(models.ProjectType)
admin.site.register(models.ProjectPriority)
admin.site.register(models.TaskPriority)
admin.site.register(models.TaskStatus)
admin.site.register(models.TaskType)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'project', 'type', 'priority')
    search_fields = ('title', 'description')
    ordering = ('priority',)
    list_filter = ('status', 'project', 'type', 'priority')


admin.site.register(models.Task, admin_class=TaskAdmin)
