# dogs/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Breed, Dog
from .forms import DogForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def index(request):
    title = 'Главная страница'
    context = {'title': title}
    return render(request, 'dogs/index.html', context)

def breeds(request):
    title = 'Породы собак'
    breeds = Breed.objects.all()
    breeds_with_dogs = {}
    for breed in breeds:
        breeds_with_dogs[breed] = Dog.objects.filter(breed=breed)
    context = {'title': title, 'breeds_with_dogs': breeds_with_dogs}
    return render(request, 'dogs/breeds.html', context)

@login_required
def dogs_list(request):
    title = 'Список ваших собак'
    dogs = Dog.objects.all()  # Получаем всех собак
    context = {'title': title, 'dogs': dogs}
    return render(request, 'dogs/dogs_list.html', context)

@login_required
def dog_create(request):
    title = 'Добавить собаку'
    form = DogForm()  # Инициализация формы
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.owner = request.user  # Связываем собаку с текущим пользователем
            dog.save()
            return redirect('dogs:dog_read', pk=dog.pk)  # Изменяем редирект на страницу с информацией о собаке
    context = {'title': title, 'form': form}
    return render(request, 'dogs/dog_create.html', context)

@login_required
def dog_update(request, pk):
    title = 'Редактировать информацию о собаке'
    dog = get_object_or_404(Dog, pk=pk, owner=request.user)  # Получаем собаку по ID и проверяем, что она принадлежит текущему пользователю
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES, instance=dog)  # Передаем instance=dog для обновления существующего объекта
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('dogs:dog_read', pk=dog.pk)  # Перенаправляем на страницу с информацией о собаке
    else:
        form = DogForm(instance=dog)  # Создаем форму с данными существующего объекта
    context = {'title': title, 'form': form, 'dog': dog}
    return render(request, 'dogs/dog_update.html', context)

@login_required
def dog_delete(request, pk):
    title = 'Удалить собаку'
    dog = get_object_or_404(Dog, pk=pk, owner=request.user)  # Получаем собаку по ID и проверяем, что она принадлежит текущему пользователю
    if request.method == 'POST':
        dog.delete()  # Удаляем собаку
        return redirect(reverse('users:user_profile'))  # Перенаправляем на страницу профиля
    context = {'title': title, 'dog': dog}
    return render(request, 'dogs/dog_delete.html', context)

def dog_read(request, pk):
    title = 'Информация о собаке'
    dog = get_object_or_404(Dog, pk=pk)
    context = {'title': title, 'dog': dog}
    return render(request, 'dogs/dog_read.html', context)

