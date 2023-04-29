from django.urls import include, path

from production import views

from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'projects', views.ProjectListView)

urlpatterns = [
    # path('', include(router.urls)),
    path('projects/', views.ProjectListView.as_view()),
    path('tasks/', views.TaskListView.as_view()),
]
