from distutils.command.config import config
from urllib import request
from django.http import JsonResponse
from django.shortcuts import redirect, render
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
        victim = Victim(name=name, email=email, password=password,
                        phone=phone, address=address, pincode=pincode)
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
        authority = Authority(
            name=name, email=email, password=password, address=address, pincode=pincode)
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
    authority = Authority.objects.get(name=request.user.username)
    complains = Complain.objects.filter(pincode=authority.pincode)
    return render(request, "authorityHome.html", {'complains': complains})


def victimLogout(request):
    logout(request)
    return HttpResponseRedirect("/victimLogin")


def authorityLogout(request):
    logout(request)
    return HttpResponseRedirect("/authorityLogin")
<<<<<<< HEAD
=======


def victimComplaint(request, id):
    if request.method == 'POST':
        subject = request.POST['subject']
        description = request.POST['description']
        date = request.POST['date']
        location = request.POST['location']
        pincode = request.POST['pincode']
        victim = Victim.objects.get(id=id)
        type = request.POST['type']
        complain = Complain(subject=subject, description=description, date=date,
                            address=location, pincode=pincode, person=victim.name, type=type)
        complain.save()
    return HttpResponseRedirect('/victimHome')


def pastComplains(request):
    complains = Complain.objects.filter(person=request.user.username)
    return render(request, "pastComplain.html", {'complains': complains})


def editComplain(request, id):
    complain = Complain.objects.get(id=id)
    if request.method == 'POST':
        scope = request.POST['scope']
        complain.scope = scope
        complain.save()
        return HttpResponseRedirect('/pastComplains')


def publicComplains(request):
    complains = Complain.objects.filter(scope="Public")
    return render(request, "publicComplains.html", {"complains": complains})


def contactAuthority(request):
    authorities = Authority.objects.all()
    return render(request, "contactAuthority.html", {'authorities': authorities})


def contactVictims(request):
    victims = Victim.objects.all()
    return render(request, "contactVictim.html", {'victims': victims})


def contactAuth(request, id):
    auth = Authority.objects.get(id=id)
    room = str(request.user.username) + str(auth.name)
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+request.user.username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+request.user.username)


def contactVict(request, id):
    vict = Victim.objects.get(id=id)
    room = str(vict.name) + str(request.user.username)
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+request.user.username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+request.user.username)


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(
        value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
>>>>>>> 7f2cc416878480badd6361bdd29a1d94cdafb7ef
