from django.shortcuts import render


def home(request, menu_name='main_menu'):
    context = {'menu_name': menu_name}
    print('bruh')
    return render(request, 'home.html', context)
