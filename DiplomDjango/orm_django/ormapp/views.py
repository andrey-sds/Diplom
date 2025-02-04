from django.contrib.auth.hashers import make_password
from django.http import HttpResponse,Http404
from django.shortcuts import render
from .forms import UserRegister
from .models import *

# Create your views here.
info = {}


def main(request):
    title = 'Главная'
    main_page = '/'
    context = {
        'title': title,
        'main_page': main_page,
    }
    return render(request, 'main.html', context)


def sign_up(request):

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают!'
            if UserProfile.objects.filter(username=username).exists():
                info['error'] = 'Пользователь уже существует!'
            else:
                try:
                    hashed_password = make_password(password)
                    UserProfile.objects.create(
                        username=username,
                        password=hashed_password,
                        firstname=firstname,
                        lastname=lastname,
                        age=age
                    )
                    info['success'] = f"Приветствуем, {username}!"
                except Exception as e:
                    info['error'] = f"Ошибка при создании пользователя: {str(e)}"

    else:
        form = UserRegister()

    context = {
        'form': form,
        'info': info

    }

    return render(request, 'register.html', context)
