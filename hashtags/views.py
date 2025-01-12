
from django.shortcuts import render
from .models import Tag, Product

def fairy_tales(request):
    if request.method == 'GET':
        fairy_tales= Product.objects.filter(tags__name='example')
        return render(request, template_name='example.html', context={'fairy_tales': fairy_tales})

def fantasy(request):
    if request.method == 'GET':
        fantasy = Product.objects.filter(tag__name='example')
        return render(request, template_name='example.html', context={'fantasy': fantasy})

def drama(request):
    if request.method == 'GET':
        drama = Product.objects.filter(tag__name='example')
        return render(request, template_name='example.html', context= {'drama': drama})
