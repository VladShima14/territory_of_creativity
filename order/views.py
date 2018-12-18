from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from creativity_app.models import Creativity
from .cart import Cart
from .forms import OrderForm


@require_POST
def cart_add(request, creativity_id):
    cart = Cart(request)
    creativity = get_object_or_404(Creativity, id=creativity_id)
    form = OrderForm(request.POST)
    return redirect('cart:CartDetail')


def cart_remove(request, creativity_id):
    cart = Cart(request)
    creativity = get_object_or_404(Creativity, id=creativity_id)
    cart.remove(creativity)
    return redirect('cart:CartDetail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
