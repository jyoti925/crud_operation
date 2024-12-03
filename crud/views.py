from django.shortcuts import render, redirect, get_object_or_404
from crud.models import Employees
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views 
def home(request):
    emp = Employees.objects.all()
    context = {
        'emp': emp,
    }
    return render (request, 'base.html', context)
def ADD(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        emp =Employees(name = name,
                       email=email,
                       address = address,
                       phone = phone)
        emp.save()
        return redirect('home')
    return render (request, 'base.html')

def Edit(request):
    emp=Employees.objects.all()
    context ={
        'emp':emp
    }
    return render (request, 'base.html', context)

def update(request, id):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')

        emp =Employees(
            id=id,
            name=name,
            email= email,
            address=address,
            phone=phone
        )
        emp.save()
        return redirect('home')
    return render(request, 'base.html')
def Delete(request, id):
    
    emp = get_object_or_404(Employees, id=id)
    emp.delete()  
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        initial_data = {'username':'', 'password1':'', 'password2':''}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'signup.html',{'form':form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'login.html',{'form':form})
    
def dashboard(request):
    pass
def logout_view(request):
    logout(request)
    return redirect('login')
    