from django.urls import path
from .views import home

urlpatterns = [
    path('<str:menu_name>/', home, name='home'),
    path('', home, name='default_home')
]
