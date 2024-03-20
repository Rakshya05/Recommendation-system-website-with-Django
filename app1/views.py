from django.shortcuts import render, HttpResponse, redirect
from app1.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

'''@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')'''

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            my_user = CustomUser.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')
def LoginPage(request):
    '''user = authenticate(email='hello123@gmail.com', password='123456')
    print(user)'''

    if request.method == 'POST':
        email = request.POST.get('email')  # Change 'username' to 'email'
        password = request.POST.get('pass')
        print(f"Email: {email}, Password: {password}")
        print(f"Request: {request}")

        user = authenticate(request, email=email, password=password)
        print(f"Authenticated User: {user}")

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Email or Password is incorrect!!!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('/')
