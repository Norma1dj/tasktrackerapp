from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        'projects': projects
    }
    return render(request, "list_projects.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    project = Project.objects.get(id=id)

    context = {
        "project": project
    }
    return render(request, 'show_project.html', context)
