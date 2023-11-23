import string

from django.core import serializers

from django import template
from django.urls import resolve
from django.utils.safestring import mark_safe

from treemenu.models import MenuItem

register = template.Library()
current_url = ''


def draw(item, submenu='', par=False):
    str = f"<ul><li class={'active' if item.url + '/' == current_url else ''}><a href=/{item.menu_name}>{item.menu_name}</a>{submenu}</li></ul>"
    if item.parent and par:
        return draw(item.parent, str)
    else:
        return str


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name, items=None):
    global current_url
    current_url = context['request'].path
    items = MenuItem.objects.filter(menu_name=menu_name)
    menu = ''
    for item in items:
        submenu = ''
        if item.childs.all():
            for child in item.childs.all():
                submenu += draw(child)
        menu += draw(item, submenu, True)

    return mark_safe(menu)
