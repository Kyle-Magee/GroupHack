from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm
# Create your views here.
def add_user(request):
    form = UserForm()
    return render(request, 'test.html', context)

def main_page(request):
    return render(request, 'main.html')

def choose_language(request):
    return render(request, 'prolang.html')