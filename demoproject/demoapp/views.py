from django.shortcuts import render,redirect
from . models import *

# Create your views here.


def home(request):
    return render(request,'home.html')


def register_model(request):
    if request.method == 'POST':
        name = request.POST['name1']
        email = request.POST['email1']
        password = request.POST['password1']
        age = request.POST['age1']
        register(name=name,email=email,password=password,age=age).save()
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email1']
        password = request.POST['password1']
        register.objects.get(email= email, password=password)
        return redirect('/table/')
    return render(request,'login.html')


def table(request):
    x = register.objects.all().order_by('name')
    return render(request,'table1.html',{'x':x})


def update_register(request,id):
    x = register.objects.get(id=id)
    if request.method == "POST":
        x.name = request.POST.get('name1')
        x.email= request.POST.get('email1')
        x.age= request.POST.get('age1')
        x.password=request.POST.get('password1')
        x.save()
        return redirect('/table/')
    return render(request, 'update.html', {'obj': x})


def delete_register(request,id):
    x = register.objects.get(id=id)
    x.delete()
    return redirect('/table/')


def first_data(request):
    y = register.objects.first()
    return render(request,'first_data.html',{'y':y})


def last_data(request):
    y = register.objects.last()
    return render(request,'last_data.html',{'y':y})


def age_calculation(request):
    age = register.objects.filter(age__gte=18)
    return render(request, 'greater.html',{'age':age})


def age_calculate_18(request):
    age = register.objects.filter(age__lte=18)
    return render(request, 'less.html',{'age':age})


def product_details(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        Rate = request.POST['Rate']
        customer = request.POST['customer']
        product(product_name=product_name,customer=customer,Rate=Rate).save()
    return render(request,'product.html')
