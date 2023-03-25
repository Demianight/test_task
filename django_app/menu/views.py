from django.shortcuts import render
from .models import Menu
from django.shortcuts import get_object_or_404
from .utils import get_tree


def index(request):
    menus = Menu.objects.filter(parent=None)
    context = {
        'menus': menus,
    }
    return render(request, 'index.html', context=context)


def render_menu(request, name):
    menu = get_object_or_404(Menu, name=name)
    childs = Menu.objects.filter(parent=menu)
    context = {
        'menu': menu,
        'childs': childs,
    }
    print(get_tree(menu))
    return render(request, 'menu.html', context=context)
