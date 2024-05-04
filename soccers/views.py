from django.shortcuts import render
from .models import Category, Soccers
# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_soccers(request, pk):
    soccer = Soccers.objects.filter(category=pk)
    context = {
        'soccer': soccer
    }
    return render(request, 'soccers.html', context=context)

def detail(request, pk):
    baller = Soccers.objects.get(pk=pk)
    context = {
        'baller': baller
    }
    print(1)
    return render(request, 'detail.html', context=context)