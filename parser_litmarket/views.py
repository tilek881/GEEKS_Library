from django.http import HttpResponse
from django.shortcuts import render
from . import models ,forms
from django.views import generic

class LitmarketListView(generic.ListView):
    template_name = 'parser/litmarket_list.html'
    context_object_name = 'litmarket'
    model = models.LitmarketParser

    def get_queryset(self):
        return self.model.objects.all()


class LitmarketFormView(generic.FormView):
    template_name = 'parser/litmarket_form.html'
    form_class = forms.LitmarketForms

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Парсинг успешен')
        else:
            return super(LitmarketFormView, self).post(request, *args, **kwargs)
