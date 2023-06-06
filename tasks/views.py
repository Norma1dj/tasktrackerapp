from django.shortcuts import render, redirect
from tasks.forms import CreateTaskForm
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required()
def create_task(request):
    
    if request.method == "POST":

        form = CreateTaskForm(request.POST)
        if form.is_valid(): 
            task = form.save()
            task.save()

            return redirect("list_projects")

    else:
        form = CreateTaskForm()

    context = {
        "form": form,
    }
    return render(request, "create_task.html", context)

# def create_task(request, project_id):
#     project = Project.objects.get(id=project_id)

#     if request.method == 'POST':
#         form = CreateTaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.project = project
#             task.save()
#             return redirect('project_list')
#     else:
#         form = CreateTaskForm()

#     return render(request, 'create_task.html', {'form': form, 'project': project})
