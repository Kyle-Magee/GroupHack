from django.forms import ModelForm 
from django import forms
from .models import User, Language, Interest

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email',  'languages', 'project_level', 'name']


class UserInterestForm(ModelForm):
    class Meta:
        model = User
        fields = ['interests']
        widgets = {'interests': forms.CheckboxSelectMultiple}

class UserLanguagesForm(ModelForm):
    class Meta:
        model = User
        fields = ['languages']

class UserNameForm(ModelForm):
    class Meta:
        model = User
        fields = ['name']

class UserEmailForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']

class UserProjectLevelForm(ModelForm):
    class Meta:
        model = User
        fields = ['project_level']