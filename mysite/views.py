from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "home.html")

def abs(request):
    return render(request, "abs.html")

def pho(request):
    return render(request, "pho.html")

def whi(request):
    return render(request, "whi.html")
