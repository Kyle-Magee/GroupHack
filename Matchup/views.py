from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Language, Interest
from .forms import UserForm, UserInterestForm, UserLanguagesForm
# Create your views here.
def add_user(request):
    form = UserForm()
    context = {'form':form}
    if request.method == 'POST':
        form = UserForm(request.POST)
        user= User(email=form.data['email'], languages = form.data.getlist('languages'), project_level=form.data['project_level'], interests=form.data.getlist('interests'),
                   name=form.data['name'])
        print(form.data.getlist('languages'))
        user.save()

    return render(request, 'test.html', context)

def main_page(request):
    return render(request, 'main.html')

def choose_language(request):
    return render(request, 'language.html')

def interest(request):
    interest_form = UserInterestForm()
    lang_form = UserLanguagesForm()
    context = {
        'interests':Interest.objects.all(),
        'interest_form':interest_form,
        'lang_form':lang_form,

    }
     
    if request.method == 'POST':
        form = UserInterestForm(request.POST)

    return render(request, 'interests.html', context)

def show_users(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'show_users.html', context)