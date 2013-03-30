# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from user.forms import LoginForm

def showLoginForm(request):
    form = LoginForm()
    return render_to_response("user/login.html",{"form":form}, RequestContext(request))
