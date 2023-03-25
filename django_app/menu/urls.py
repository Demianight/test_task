from django.urls import path
from .views import index, render_menu


app_name = 'menu'

urlpatterns = [
    path('', index, name='index'),
    path('<str:name>', render_menu, name='menu'),
]
