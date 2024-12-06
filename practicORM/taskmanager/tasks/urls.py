from django.urls import path

from tasks import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('performers/', views.performers, name='performers'),
    path('tasks/', views.tasks, name='tasks'),
    path('project/<int:project_id>', views.project, name='project')
]