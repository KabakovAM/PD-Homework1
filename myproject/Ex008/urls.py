from django.urls import path
from . import views

urlpatterns = [
    path('about_django/', views.about_django, name='django'),
    path('about_me/', views.about_m, name='me')
]