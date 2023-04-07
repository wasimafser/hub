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
