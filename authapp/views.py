from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # trying to login user in
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("crud:home")
        
        # if the username if correct, error password incorrect
        if User.objects.filter(username=username).exists():
            messages.error(request, "Your password is incorrect!")
            return redirect("auth:login")
        else:
            # Error both username and password incorrect.
            messages.error(request, "The username and password provided is invalid")
            return redirect("auth:login")
            
    return render(request, "authapp/login.html")


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        
        if password == password2:
            # Check the email already exits
            if User.objects.filter(email=email).exists():
                messages.error(request, f"'{email}' is already in use by another user")
                return redirect("auth:signup")
            if User.objects.filter(username=username).exists():
                messages.error(request, f"'{username}' is already in use by another user")
                return redirect("auth:signup")
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            
            account_creation_msg = "Account creation was successful. Please login"
            return render(request, "authapp/login.html", {"account_creation_msg": account_creation_msg})
        
        messages.error(request, "The two passwords do not match!")
        return redirect("auth:signup")
    return render(request, "authapp/signup.html")