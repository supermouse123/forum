from django.shortcuts import render, HttpResponse

# Create your views here.

def user_model(request):
    return HttpResponse("this is user")


def login(request):
    return HttpResponse("this is login")

def register(request):
    return HttpResponse("this is register")