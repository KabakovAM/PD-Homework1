from django.shortcuts import render
from django.http import HttpResponse
import random
import logging

logger = logging.getLogger(__name__)

def coin(request):
    a = random.choice(['Орёл', 'Решка'])
    logger.info(f'Выпал {a}')
    return HttpResponse(a)

def cube(request):
    a = random.randint(1,6)
    logger.info(f'Выпал {a}')
    return HttpResponse(a)

def num(request):
    a = random.randint(0,100)
    logger.info(f'Выпал {a}')
    return HttpResponse(a)
