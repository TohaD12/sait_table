from .models import Task, Accessories
from .forms import TaskForm, AccessoriesForm
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
            obj = form.save(commit=False)
            if obj.after_adjustment_quantity_actual == "":
                obj.after_adjustment_quantity_actual = obj.quantity_actual
            else:
                obj.after_adjustment_quantity_actual = obj.after_adjustment_quantity_actual

            if obj.after_adjustment_quantity_1c == "":
                if obj.adjustments != "0" and obj.adjustments != "":
                    obj.after_adjustment_quantity_1c = str(int(obj.quantity_1c) + int(obj.adjustments))
                    if int(obj.adjustments) >= 1 and int(obj.delta) >= 1:
                        obj.after_adjustment_delta = str(int(obj.delta) - int(obj.adjustments))
                    elif int(obj.adjustments) <= -1 and int(obj.delta) <= -1:
                        obj.after_adjustment_delta = str(int(obj.delta) - int(obj.adjustments))
                    elif int(obj.adjustments) <= -1 and int(obj.delta) >= 1:
                        obj.after_adjustment_delta = str(int(obj.delta) + int(obj.adjustments))
                    elif int(obj.adjustments) >= 1 and int(obj.delta) <= -1:
                        obj.after_adjustment_delta = str(int(obj.delta) + int(obj.adjustments))
            else:
                obj.after_adjustment_quantity_1c = obj.after_adjustment_quantity_1c

            if obj.after_adjustment_delta == "":
                obj.after_adjustment_delta = obj.delta
            else:
                obj.after_adjustment_delta = obj.after_adjustment_delta
            obj.save()

    form = TaskForm()
    name = Task.objects.filter().order_by('-id')[:1]
    context = {
        'form': form,
        'name': name
    }
    return render(request, 'main/create.html', context)


def create_accessories(request):
    if request.method == 'POST':
        form = AccessoriesForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if obj.after_adjustment_quantity_actual == "":
                obj.after_adjustment_quantity_actual = obj.quantity_actual
            else:
                obj.after_adjustment_quantity_actual = obj.after_adjustment_quantity_actual

            if obj.after_adjustment_quantity_1c == "":
                obj.after_adjustment_quantity_1c = obj.quantity_1c
            else:
                obj.after_adjustment_quantity_1c = obj.after_adjustment_quantity_1c

            if obj.after_adjustment_delta == "":
                obj.after_adjustment_delta = obj.delta
            else:
                obj.after_adjustment_delta = obj.after_adjustment_delta

            obj.save()

    form = AccessoriesForm()
    name = Accessories.objects.filter().order_by('-id')[:1]
    context = {
        'form': form,
        'name': name
    }
    return render(request, 'main/create_accessories.html', context)

#
# def create_accessories(request):
#     name = Accessories.objects.all()
#     return render(request, 'main/create_accessories.html', {'name': name})


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
