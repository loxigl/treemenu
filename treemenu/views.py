from django.shortcuts import render


def home(request, menu_name='main_menu'):
    context = {'menu_name': menu_name}
    return render(request, 'home.html', context)
