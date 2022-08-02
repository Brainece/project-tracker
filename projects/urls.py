"""Defines urls for projects"""

from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('projects/',views.projects, name='projects'),
    path('projects/<int:project_id>/',views.project, name='project'),
    path('new_project/', views.new_project, name='new_project'),
    path('new_task/<int:project_id>/', views.new_task, name='new_task'),
]