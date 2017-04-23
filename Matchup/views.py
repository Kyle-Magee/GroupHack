from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm
# Create your views here.
def add_user(request):
    form = UserForm()
    return render(request, 'test.html', {'form':form})