from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm, UserForm, ManyFieldsForm, ManyFieldsFormWidget
from .models import User
from django.core.files.storage import FileSystemStorage





def index(request):
    'Ответ на основе функции'

    return HttpResponse('Hello def')


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            print(f'---------------Данные формы {name} {email} {age}')
    else:
        form = UserForm()
    return render(request, 'app4/user_form.html', {'form':form})


def many_fields_form(request):
    if request.method == 'POST':
        # form = ManyFieldsForm(request.POST)
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            print(f'---------------Данные большой формы прошли проверку на валидность ')
    else:
        # form = ManyFieldsForm()
        form = ManyFieldsFormWidget()
    return render(request, 'app4/many_fields_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            print(f'---------------Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'app4/user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'app4/upload_image.html', {'form':form})
