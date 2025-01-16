from django.shortcuts import render
from .models import Tag, Product

def all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, template_name='hashtags/all_products.html', context={'products': products})

def fairy_tale(request):
    if request.method == 'GET':
        fairy_tale = Product.objects.filter(tags__name='fairy tale')
        return render(request, template_name='hashtags/fairy_tale.html', context={'fairy_tale': fairy_tale})

def fantasy(request):
    if request.method == 'GET':
        fantasy = Product.objects.filter(tags__name='fantasy')
        return render(request, template_name='hashtags/fantasy.html', context={'fantasy': fantasy})

def drama(request):
    if request.method == 'GET':
        drama = Product.objects.filter(tags__name='drama')
        return render(request, template_name='hashtags/drama.html', context={'drama': drama})


