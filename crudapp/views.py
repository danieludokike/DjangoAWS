from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



@login_required(login_url="auth:login")
def home_view(request):
    return HttpResponse("<h1> Django CRUD APP. Coming soon page. </h1>")
