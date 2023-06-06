from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import CreateProjectForm

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

@login_required
def create_project(request):

    if request.method == "POST":

        form = CreateProjectForm(request.POST)
        if form.is_valid(): 
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("list_projects")
    else:
        form = CreateProjectForm()

    context = {
        "form": form,
    }
    return render(request, "create_project.html", context)