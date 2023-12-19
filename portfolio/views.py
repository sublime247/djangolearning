from django.shortcuts import render , redirect

# Create your views here.
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm



def projects(request):
    project = Project.objects.all()
    context = { 'projlst': project}
    return render(request,  'temps1.html', context, )

def project1(request, pk):
    projectObj = Project.objects.get(id=pk)
    tag =projectObj.tags.all()
    return render(request,   'temps2.html', {'project': projectObj, 'tags': tag} )


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, 'project_form.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form':form}
    return render(request, 'project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request, 'delete_template.html', context)

