from .models import Task, Accessories
from .forms import TaskForm, AccessoriesForm
from django.db.models import Q
from django.shortcuts import render


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'details_name': 'Главная страница сайта', 'tasks': tasks})


def home_accessories(request):
    accessories = Accessories.objects.all()
    return render(request, 'main/home_accessories.html', {'details_name': 'Главная страница сайта',
                                                          'accessories': accessories})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


def create_accessories(request):
    if request.method == 'POST':
        form = AccessoriesForm(request.POST)
        if form.is_valid():
            form.save()

    form = AccessoriesForm()
    context = {
        'form': form
    }
    return render(request, 'main/create_accessories.html', context)


def search(request):
    queryset = request.GET.get('q', '')
    queryset = queryset.split()

    if queryset:
        try:
            task = Task.objects.filter(code__exact=queryset[0], color_code__exact=queryset[1])
        except IndexError:
            task = Task.objects.filter(code__exact=queryset[0])

    else:
        task = Task.objects.all()
    return render(request, 'main/search.html', {'details_name': 'Главная страница сайта', 'task': task})


def search_accessories(request):
    queryset = request.GET.get('q', '')

    if queryset:
        try:
            task = Accessories.objects.filter(code__iexact=queryset)
        except AttributeError:
            print("abra kadabra")

    else:
        task = Accessories.objects.all()
    return render(request, 'main/search_accessories.html', {'details_name': 'Главная страница сайта', 'task': task})

