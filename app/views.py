from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show(request):
    return HttpResponse("<h2>WELCOME YOGESH.. YOU HAVE CRACKED IT...</h2>")
