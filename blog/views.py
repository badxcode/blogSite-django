from django.shortcuts import render, HttpResponseRedirect

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
def signup(request):
    return render(request, 'blog/signup.html')

# login
def user_login(request):
    return render(request, 'blog/login.html')

# logout
def user_logout(request):
    return HttpResponseRedirect('/')