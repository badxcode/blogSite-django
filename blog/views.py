from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages

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
    form = LoginForm()
    return render(request, 'blog/login.html', {'form':form})

# logout
def user_logout(request):
    return HttpResponseRedirect('/')