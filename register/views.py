from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/myaccount/")
        
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form': form})
