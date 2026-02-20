from django.shortcuts import render, get_object_or_404
from .models import Project
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from rest_framework import generics, permissions

def project_list(request):
    projects = Project.objects.all()

    # split tech stack here (Python allowed)
    for project in projects:
        project.tech_list = project.tech_stack.split(',')

    return render(request, "projects/project_list.html", {
        "projects": projects
    })



def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    project.tech_list = project.tech_stack.split(',')
    return render(request, "projects/project_detail.html", {
        "project": project
    })

class ProjectListAPI(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by('-created_date')
    serializer_class = ProjectSerializer

    # Only logged-in users can add
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# GET single project
class ProjectDetailAPI(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "slug"