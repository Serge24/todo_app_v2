"""
URL configuration for todo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# urls.py
from django.urls import path
from todo.views import RegisterView
from todo.views import LoginView
from todo.views import LogoutView, TaskCommentView
from todo.views import ProjectListCreateView, ProjectDetailView, TaskListCreateView, TaskDetailView, ProjectTaskListCreateView,TaskStatusUpdateView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', obtain_auth_token, name='login'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    
    #Projects routes
    path('api/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    #Tasks routes
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    #Routes additionnelles
    path('api/projects/<int:project_id>/tasks/', ProjectTaskListCreateView.as_view(), name='project-tasks'),
    path('api/tasks/<int:pk>/status/', TaskStatusUpdateView.as_view(), name='task-status-update'),
    path('api/tasks/<int:id>/comments', TaskCommentView.as_view(), name='task-comments'),
]
