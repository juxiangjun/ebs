import uuid, os
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _

class LoginForm(forms.Form):
    user_name = forms.CharField(required=True,\
        label = _("login.user_name"),\
        widget = forms.TextInput(attrs={'class':'text'})\
        )   
    password = forms.CharField(required=True,\
        label = _("login.password"),\
        widget=forms.PasswordInput(attrs={'class':'text'}))
