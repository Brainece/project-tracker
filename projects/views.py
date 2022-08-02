from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Project, Task
from .forms import ProjectForm, TaskForm

# Create your views here.
def index(request):
    """The home page for projects"""
    return render(request, 'projects/index.html')

@login_required
def projects(request):
    """Show all projects"""
    projects = Project.objects.filter(owner=request.user).order_by('creation_date')
    context = { 'projects': projects }
    return render(request, 'projects/projects.html', context)
    
@login_required
def project(request, project_id):
    """Show a single project and list all its entries"""
    project = Project.objects.get(id=project_id)
    if project.owner != request.user:
        raise Http404
    tasks = project.task_set.order_by("id")
    context = {
        'project': project,
        'tasks': tasks
    }

    return render(request,'projects/project.html',context)

@login_required
def new_project(request):
    """Add a new project"""
    if(request.method != 'POST'):
        # No data submitted, process data
        form = ProjectForm()
    else:
        # Post data submitted, process data
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            nwe_topic = form.save(commit=False)
            form.save()
            return redirect('projects:projects')

    context = {'form': form}
    return render(request,'projects/new_project.html', context)

@login_required
def new_task(request, project_id):
    """Add a new task to a particular project"""
    project = Task.objects.get(id=project_id)

    if(request.method != 'POST'):
        ## No data submitted; create a blank form\
        form = TaskForm()
    else:
        # Post data submitted; process data
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.project = project
            new_task.save()
            return redirect('projects:project', project_id=project_id)
        
    ## Displays a blank or invalid form
    context = {'project': project, 'form': form}
    return render(request, "projects/new_task.html", context)




