from django import template
from wallpapers.models import Categories, Wallpapers
from django.contrib.contenttypes.models import ContentType
from datetime import timedelta, datetime
from django.db.models import *


register = template.Library()


@register.simple_tag()
def wallpapers_count():
    return Wallpapers.objects.count()


@register.simple_tag()
def last_updated_date():
    from wallpapers.models import Wallpapers
    # Просто берем дату последнего добавленного элемента напрямую из таблицы обоев
    last_wallpaper = Wallpapers.objects.order_by('-created_up').first()
    if last_wallpaper:
        return last_wallpaper.created_up.strftime("%d.%m.%Y")
    return "Нет данных"


# Получаем ВСЕ категории и кол-во записей в каждой
@register.simple_tag
def get_categories():
    return Categories.objects.annotate(Count('wallpapers')).order_by('name_category')


# Получаем категорию в которой находимся сейчас и кол-во записей в ней
@register.simple_tag(takes_context=True)
def get_category_info(context):
    request = context['request']
    category_id = request.resolver_match.kwargs.get('category_id')
    category = Categories.objects.get(id=category_id)
    entry_count = Wallpapers.objects.filter(id_category=category).count()
    return {'category': category, 'entry_count': entry_count}
