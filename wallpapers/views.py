from django.http import Http404
from django.shortcuts import render, get_object_or_404
from wallpapers.models import Wallpapers, Categories, Tags, Wallpapers_Tags
from django.core.paginator import Paginator
from django.db.models import Count


def index(request):
    wallpapers = Wallpapers.objects.all()
    paginator = Paginator(wallpapers, 50)
    page_number = request.GET.get('page')
    if page_number == None: page_number = 1
    page_obj = paginator.get_page(page_number)
    # Проверяем, не выходит ли запрашиваемая страница за пределы допустимого диапазона
    if int(page_number) > paginator.num_pages:
        raise Http404("Page not found")
    return render(request, 'wallpapers/home.html', {'page_obj': page_obj})


def random_wallps(request):
    random_records = Wallpapers.objects.all().order_by('?')[:50]
    return render(request, 'wallpapers/home.html', {'page_obj': random_records})


def get_categories(request, category_id):
    # Проверяем наличие категории в базе данных
    try:
        category = Categories.objects.get(id=category_id)
    except Categories.DoesNotExist:
        raise Http404("Category does not exist")
    wallpapers = Wallpapers.objects.filter(id_category_id=category_id)
    paginator = Paginator(wallpapers, 50)
    page_number = request.GET.get('page')
    if page_number == None: page_number = 1
    page_obj = paginator.get_page(page_number)
    # Проверяем, не выходит ли запрашиваемая страница за пределы допустимого диапазона
    if int(page_number) > paginator.num_pages:
        raise Http404("Page not found")
    return render(request, 'wallpapers/cat.html', {'page_obj': page_obj})


def view_wallp(request, wallp_id):
    wallp = get_object_or_404(Wallpapers, pk=wallp_id)
    tag_ids = wallp.wallpapers_tags_set.values_list('tag_id', flat=True)
    tags = Tags.objects.filter(id__in=tag_ids)
    return render(request, 'wallpapers/wallp.html', {'wallp': wallp, 'tags': tags})


def tag_list(request):
    # Выбираем только те тэги с которыми количество записей > 99. т.к.
    # количество тэгов в базе > 22 000 и много тэгов имеют по 1-5 связанных записей
    tags = Tags.objects.annotate(wallpaper_count=Count('wallpapers_tags')).filter(wallpaper_count__gt=99).order_by('-wallpaper_count')
    return render(request, 'wallpapers/tags.html', {'tags': tags})


def wallpapers_by_tag(request, tag_id):
    try:
        tag = Tags.objects.get(id=tag_id)
    except Tags.DoesNotExist:
        raise Http404("Tag does not exist")
    tag = Tags.objects.get(id=tag_id)
    wallpapers = Wallpapers.objects.filter(wallpapers_tags__tag_id=tag)
    paginator = Paginator(wallpapers, 50)
    page_number = request.GET.get('page')
    if page_number == None: page_number = 1
    page_obj = paginator.get_page(page_number)
    # Проверяем, не выходит ли запрашиваемая страница за пределы допустимого диапазона
    if int(page_number) > paginator.num_pages:
        raise Http404("Page not found")
    wallps_count = wallpapers.count()
    context = {
        'tag': tag,
        'page_obj': page_obj,
        'wallps_count': wallps_count,
    }
    return render(request, 'wallpapers/wallps_tags.html', context)


def search(request):

    s = request.GET.get('s')

    try:
        s_first_capital = s.capitalize()
        tags = Tags.objects.filter(tag_name__icontains=s_first_capital)
        wallpapers_first_capital = Wallpapers.objects.filter(wallpapers_tags__tag_id__in=tags)
    except Tags.DoesNotExist:
        wallpapers_first_capital = Wallpapers.objects.none()

    try:
        s_upper = s.upper()
        tags = Tags.objects.filter(tag_name__icontains=s_upper)
        wallpapers_upper = Wallpapers.objects.filter(wallpapers_tags__tag_id__in=tags)
    except Tags.DoesNotExist:
        wallpapers_upper = Wallpapers.objects.none()

    try:
        s_lower = s.lower()
        tags = Tags.objects.filter(tag_name__icontains=s_lower)
        wallpapers_lower = Wallpapers.objects.filter(wallpapers_tags__tag_id__in=tags)
    except Tags.DoesNotExist:
        wallpapers_lower = Wallpapers.objects.none()

    wallpapers = (wallpapers_first_capital | wallpapers_lower | wallpapers_upper).distinct()
    search_count = wallpapers.count

    paginator = Paginator(wallpapers, 50)
    page_number = request.GET.get('page')
    if page_number == None: page_number = 1
    page_obj = paginator.get_page(page_number)
    # Проверяем, не выходит ли запрашиваемая страница за пределы допустимого диапазона
    if int(page_number) > paginator.num_pages:
        raise Http404("Page not found")
    return render(request, 'wallpapers/search.html', {'page_obj_s': page_obj,
                                                      's': s,
                                                      'search_count': search_count})

