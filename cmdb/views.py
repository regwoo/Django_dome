from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.



def index(request):
    #request.POST
    #request.POST
    return HttpResponse("hello World!")
