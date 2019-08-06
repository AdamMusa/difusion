from django.shortcuts import render, redirect
from client.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create(
                username = data['username'],
                email = data['email'],
            )

            new_user.set_password(data['password'])
            new_user.save()
            messages.success(request,'account created with succesful')
            return redirect('projet:index')
    context = {
        'form':form
    }
    

    return render(request, 'client/register.html', context)
   

#Connexion func

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(username=username, password=password)

            if user:
                auth_login(request, user)
                return redirect('projet:index')

            
    context = {
            'form':form
        }

    return render(request, 'client/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('projet:index')