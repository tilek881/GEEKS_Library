from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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