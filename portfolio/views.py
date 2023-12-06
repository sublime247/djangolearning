from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

project_list = [
    {"id": '1', "title": "Project A", "name": "Alpha"},
    {"id": '2', "title": "Project B", "name": "Beta"},
    {"id": '3', "title": "Project C", "name": "Charlie"},
    {"id": '4', "title": "Project D", "name": "Delta"},
    {"id": '5', "title": "Project E", "name": "Echo"}
]

def projects(request):
    title = 'Not tired'
    name = 'ADEOLA'
    num = 10
    context = {'message':title, 'msg':name, 'number': num, 'projlst': project_list}
    return render(request,  'temps1.html', context, )
def project1(request, pk):
    projectObj = None
    for i in project_list:
      if i['id']==pk:
         projectObj = i
    return render(request,   'temps2.html', {'project': projectObj} )

