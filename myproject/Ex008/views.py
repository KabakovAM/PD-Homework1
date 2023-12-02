# from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def about_django(request):
    html = '<h1>Джанго</h1>\
        Это свободный фреймворк для веб-приложений на языке Python,<br>\
        использующий шаблон проектирования MVC.<br>\
        Проект поддерживается организацией Django Software Foundation.'
    return HttpResponse(html)

def about_me(request):
    html = '<h1>Кабаков Антон Михайлович</h1>\
        Студент GeekBrains'
    return HttpResponse(html)
