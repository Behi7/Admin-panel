from django.shortcuts import render, redirect
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    img = models.Imageuser.objects.last()
    count = len(models.Employees.objects.all())
    return render(request, 'dashboard/index.html', {'img':img, 'count':count})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboards')
        else:
            return redirect('login')
    return render(request, 'dashboard/login.html')

def log_out(request):
    logout(request)
    return redirect('login')


def table(request):
    context = {}
    employes = models.Employees.objects.all()
    img = models.Imageuser.objects.last()
    context['employes'] = employes
    context['img'] = img
    return render(request, 'dashboard/employes.html', context)

def vizit(request):
    attendances = models.Attendance.objects.all().order_by('-visit_time')
    img = models.Imageuser.objects.last()
    return render(request, 'dashboard/vizit.html', {'attendances':attendances, 'img':img})


def update(request, id):
    context = {}
    employes = models.Employees.objects.get(id=id)
    context['employes'] = employes
    if request.method == "POST":
        employes.l_name = request.POST['l_name']
        employes.f_name = request.POST['f_name']
        employes.age = request.POST['age']
        employes.work = request.POST['work']
        if 'image' in request.FILES:
            employes.images = request.FILES['image']
        employes.save()
        return redirect('table')
    return render(request, 'dashboard/updateemploy.html', context)

def create(request):
    if request.method == "POST":
        models.Employees.objects.create(
            f_name = request.POST['f_name'],
            l_name = request.POST['l_name'],
            age = request.POST['age'],
            work = request.POST['work'],
            phone = request.POST['phone']
        )
        return redirect('table')
    return render(request, 'dashboard/updateemploy.html')

def delete(request, id):
    models.Employees.objects.get(id=id).delete()
    return redirect('table')

def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        user = request.user
        if 'img' in request.FILES:
            models.Imageuser.objects.create(
                img = request.FILES['img']
            )

        if user.check_password(old_password):
            usernameup = request.POST.get('usernameup')
            user.username = usernameup
            user.save()

        if 'confirm_password' in request.POST:
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if not user.check_password(old_password):
                return redirect('userupdate')

            if new_password != confirm_password:
                return redirect('userupdate')

            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
        return redirect('dashboards')
        

    return render(request, 'dashboard/userupdate.html')
