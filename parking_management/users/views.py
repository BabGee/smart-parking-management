from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Succesfully Created user {username}. You can now login')
            return redirect('login')

    else:
        form = UserCreationForm()

    context = {
        'form' : form
    }
    return render(request, 'users/signup.html', context)


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_authenticated:
                messages.success(request, f'User {username} Successfully Logged in')
                return redirect('index')
            
        else:
            messages.warning(request, 'invalid Credentials')


    context = {
        'form': form
    }    
    return render(request, 'users/login.html', context)                        


def user_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('login')
