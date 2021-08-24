from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse

def home(request):
	

  return render(request, "home.html")


