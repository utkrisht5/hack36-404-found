from re import sub
from urllib import request
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *
# Create your views here.
def index(request):
    return render(request, "index.html")

def victimSignup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        address = request.POST['address']
        pincode = request.POST['pincode']
        user = User.objects.create_user(name, email, password)
        victim = Victim(name=name, email=email, password=password, phone=phone, address=address, pincode=pincode)
        victim.save()
    return render(request, "victimSignup.html")

def victimLogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/victimHome")
        else:
            return HttpResponseRedirect("/victimLogin")
    return render(request, "victimLogin.html")

def authoritySignup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        pincode = request.POST['pincode']
        user = User.objects.create_user(name, email, password)
        authority = Authority(name=name, email=email, password=password, address=address, pincode=pincode)
        authority.save()
    return render(request, "authoritySignup.html")

def authorityLogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/authorityHome")
        else:
            return HttpResponseRedirect("/authorityLogin")
    return render(request, "authorityLogin.html")

def victimHome(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect("/victimLogin")
    return render(request, "victimHome.html", {'victim': request.user})

def authorityHome(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect("/authorityLogin")
    complains = Complain.objects.all()
    return render(request, "authorityHome.html", {'complains': complains})

def victimLogout(request):
    logout(request)
    return HttpResponseRedirect("/victimLogin")

def authorityLogout(request):
    logout(request)
    return HttpResponseRedirect("/authorityLogin")

def victimComplaint(request, id):
    if request.method == 'POST':
        subject = request.POST['subject']
        description = request.POST['description']
        date = request.POST['date']
        location = request.POST['location']
        pincode = request.POST['pincode']
        victim = Victim.objects.get(id=id)
        complain = Complain(subject=subject, description=description,date=date,address=location,pincode=pincode,person=victim)
        complain.save()
    return HttpResponseRedirect('/victimHome')