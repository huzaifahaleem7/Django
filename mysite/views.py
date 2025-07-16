from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello This is home page")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("Hello This is about Page")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("Hello This is contact page")
    return render(request, 'contact.html')