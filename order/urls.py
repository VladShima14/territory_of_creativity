from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.cart_detail, name='CartDetail'),
    url(r'^remove/(?P<creativity_id>\d+)/$', views.cart_remove, name='CartRemove'),
    url(r'^add/(?P<creativity_id>\d+)/$', views.cart_add, name='CartAdd'),

]
