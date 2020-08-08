from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .forms import RegisterForm


def register(request):
    if request.user.is_authenticated:    
        
        return HttpResponseRedirect(reverse('home:logged_in'))
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('../login/')
        else:
            form = RegisterForm()
        return render(request, 'registration/create_account.html', {'form': form})


def you_are_loged_in(request):
    return render(request, 'home/logged_in.html')


def you_are_not_loged_in(request):
    return render(request, 'home/not_login_yet.html')


def index(request):
    return render(request, 'home/index.html')
