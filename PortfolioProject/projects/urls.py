from django.urls import path
from . import views

urlpatterns = [

    # API FIRST
    path('api/', views.ProjectListAPI.as_view(), name='projects_api'),
    path('api/<slug:slug>/', views.ProjectDetailAPI.as_view(), name='project_api_detail'),

    # WEBSITE ROUTES
    path('', views.project_list, name='projects'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
]
