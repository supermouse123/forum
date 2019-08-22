from django.shortcuts import render,HttpResponse

# Create your views here.


def post_model(request):
    return HttpResponse("this is post")

def create_post(request):
    return HttpResponse("this is create post")
