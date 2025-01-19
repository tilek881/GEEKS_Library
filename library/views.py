from django.http import HttpResponse
from datetime import datetime
from . import models
from django.views import generic


class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return models.Books.objects.filter(title__icontains=query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['q'] = query
        return context






class BooksListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'books_lists'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'
    model = models.Books


def about_me(request):
    if request.method == 'GET':
        text = """
        Привет! Меня зовут Тилек, мне 19 лет.  
        Я увлекаюсь программированием и играми.  
        Занимаюсь спортом и изучаю немецкий язык. 💻🎮🏋️‍♂️🇩🇪
        """
        return HttpResponse(text)

def about_my_pets(request):
    if request.method == 'GET':
        text = """
        У меня есть замечательный котяра по имени Luna. 🐾  
        Она обожает играть с игрушками, особенно с мячиками.  
        Luna ласковая и любит спать. 😻
        """
        image_html = "<img src='https://media.tenor.com/L5wtm55bKhQAAAAM/cute-cat.gif' style='width:350px; height:400;'>"
        full_content = f"<p>{text}</p>{image_html}"
        return HttpResponse(full_content)

def date_time(request):
    if request.method == 'GET':
        now = datetime.now()
        time_string = now.strftime("%H:%M:%S")
        return HttpResponse(f"Настоящее время🕔: {time_string}⏰")