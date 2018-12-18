from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from order.forms import OrderForm
from .models import Creativity, Category, SubCategory, Album, Photo
# Create your views here.


# TODO: Create new Query for Category/Subcategory/Creativity
def creativity_catalog(request, subcategory_slug=None):
    subcategory = None
    galka = None
    category = Category.objects.all()
    creativities = Creativity.objects.all()
    if subcategory_slug:
        galka = True
        subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        creativities = creativities.filter(subcategory=subcategory)
    return render(request, 'creativity_app/balloons.html', {
        'subcategory': subcategory,
        'category': category,
        'creativities': creativities,
        'galka': galka,
    })


def creativity_detail(request, slug, pk):
    creativities = Creativity.objects.all()
    creativity = get_object_or_404(creativities, pk=pk)
    other_offers = creativities.filter(subcategory__slug=slug).exclude(pk=creativity.pk)
    order_form = OrderForm()
    slides = []
    try:
        albums = creativity.album.get(creativity=creativity.pk)
        photos = albums.photo.all()
        for item in photos:
            slides.append(item.image)
    except ObjectDoesNotExist:
        slides = []

    return render(request, 'creativity_app/balloon-page.html', {
        'creativity': creativity,
        'other_offers':  other_offers,
        'slides': slides,
        'slides_count': len(slides),
        'order_form': order_form,
    })
