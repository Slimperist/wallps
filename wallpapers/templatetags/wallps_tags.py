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
    model_name = 'Wallpapers'
    model_class = ContentType.objects.get(app_label='wallpapers', model=model_name.lower()).model_class()
    last_updated = model_class.objects.latest('created_up').created_up
    now = datetime.now()
    # Если дата обновления равна текущей дате, выводим "сегодня в час:минуты"
    if last_updated.date() == now.date():
        return f"Сегодня в {last_updated.strftime('%H:%M')}"
    # Если дата обновления была вчера, выводим "вчера в час:минуты"
    elif last_updated.date() == now.date() - timedelta(days=1):
        return f"Вчера в {last_updated.strftime('%H:%M')}"
    # Если дата обновления была в этом году
    elif last_updated.year == now.year:
        return last_updated.strftime("%d %B в %H:%M")
    # Во всех остальных случаях выводим дату и время обновления в полном формате "день месяца год в час:минуты"
    else:
        return last_updated.strftime("%d %B %Y в %H:%M")


# Получаем ВСЕ категории и кол-во записей в каждой
@register.simple_tag
def get_categories():
    return Categories.objects.annotate(Count('wallpapers')).order_by('name_category_ru')


# Получаем категорию в которой находимся сейчас и кол-во записей в ней
@register.simple_tag(takes_context=True)
def get_category_info(context):
    request = context['request']
    category_id = request.resolver_match.kwargs.get('category_id')
    category = Categories.objects.get(id=category_id)
    entry_count = Wallpapers.objects.filter(id_category=category).count()
    return {'category': category, 'entry_count': entry_count}
