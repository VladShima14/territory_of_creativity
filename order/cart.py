from django.utils import timezone
from django.conf import settings
from creativity_app.models import Creativity


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart = cart

    def add(self, creativity):
        creativity_id = str(creativity.id)
        if creativity_id not in self.cart:
            self.cart[creativity_id] = {
                'order_time': str(timezone.now())
            }
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, creativity):
        creativity_id = str(creativity.id)
        if creativity_id in self.cart:
            del self.cart[creativity_id]
            self.save()
