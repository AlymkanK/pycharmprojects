from django.urls import path

from webapp.views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

app_name = 'webapp'

urlpatterns = [
    path('projects', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('create_projects', ProjectCreateView.as_view(), name='create_project'),
    path('projects/<int:pk>/update', ProjectUpdateView.as_view(), name='update_project'),
    path('projects/<int:pk>/delete', ProjectDeleteView.as_view(), name='delete_project')
    ]