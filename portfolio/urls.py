from django.urls import path
from . import views 


urlpatterns = [
    path('', views.projects, name='projects'),
    path('project1/<str:pk>/', views.project1, name='project1'),
    path('create-project/', views.createProject, name= 'create-project')
    # path('admin/', admin.site.urls),
]