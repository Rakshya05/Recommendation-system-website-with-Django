from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from app1.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from contactapp.models import contacts


# Create your views here.
def CreateMessage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        queryset = contacts.objects.create( email=email, message=message)
        queryset.save()

    return render(request, 'contact.html')
def AboutusPage(request):
    return render(request, 'about.html')





