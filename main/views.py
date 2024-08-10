from django.shortcuts import render, redirect
from . import models

def index(request):
    employes = models.Employees.objects.all()
    context = {}
    context['employes'] = employes
    return render(request, 'main/index.html', context)

def createVisit(request, id):
    employe = models.Employees.objects.get(id=id)
    models.Attendance.objects.create(
        employ = employe
    )
    return redirect('index')