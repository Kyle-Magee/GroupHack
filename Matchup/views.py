from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Language, Interest
from .forms import UserForm, UserInterestForm, UserLanguagesForm, UserNameForm, UserEmailForm, UserProjectLevelForm
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
    name_form = UserNameForm()
    email_form = UserEmailForm()
    level_form = UserProjectLevelForm()
    context = {
        'interests':Interest.objects.all(),
        'interest_form':interest_form,
        'lang_form':lang_form,
        'p_form':level_form,
        'e_form':email_form,
        'n_form':name_form
    }
     
    if request.method == 'POST':
        inter_f = UserInterestForm(request.POST)
        lang_f = UserLanguagesForm(request.POST)
        name_f = UserNameForm(request.POST)
        email_f = UserEmailForm(request.POST)
        level_f = UserProjectLevelForm(request.POST)

        user= User(email=email_f.data['email'], languages = lang_f.data.getlist('languages'), project_level=level_f.data['project_level'], interests=inter_f.data.getlist('interests'),
                   name=name_f.data['name'])
        user.save()

    return render(request, 'interests.html', context)

def show_users(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'matchList.html', context)