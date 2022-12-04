from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# home
def home(request):
    return render(request, 'blog/home.html')

# contact
def contact(request):
    return render(request, 'blog/contact.html')

# dashboard
def dashboard(request):
    return render(request, 'blog/dashboard.html')

# signup
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! You have become an author. Log in to continue.')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})

# login
def user_login(request):
    if not request.user.is_authenticated: # if user is already not logged in
        if request.method == "POST": 
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/dashboard/')
        else: 
            form = LoginForm()
        return render(request, 'blog/login.html', {'form':form}) # load the login template
    else:
        return HttpResponseRedirect('/dashboard/')

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')