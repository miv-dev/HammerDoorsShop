from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render

from doors.models import Door, CTA


# Create your views here.
def index(request):
    doors = Door.objects.order_by('popular')[:10]
    try:
        cta = CTA.objects.get(show=True)
    except ObjectDoesNotExist:
        cta = CTA.objects.first()
    return render(request, "pages/index.html", context={'doors': doors, 'cta': cta, 'title': 'Главная'})


def detail(request, pk=1):
    door = Door.objects.all()[pk - 1]
    return render(request, "pages/detail.html", context={'door': door, 'title': door.title})


def catalog(request):
    page_number = request.GET.get('page')
    doors = Door.objects.all()
    p = Paginator(doors, 9)
    page = p.get_page(page_number)
    return render(request, 'pages/catalog.html', context={'page': page, 'door_count': len(doors), 'title': 'Каталог'})


def contacts(request):
    return render(request, 'pages/contacts.html', context={'title': 'Контакты'})
