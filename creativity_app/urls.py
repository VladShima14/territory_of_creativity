from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="creativity_app/index.html")),
    url(r'^catalog/$', views.creativity_catalog, name="MainPage"),
    url(r'^catalog/(?P<subcategory_slug>[-\w]+)/$', views.creativity_catalog, name='SubCategoryCreativeList'),
    url(r'^catalog/(?P<slug>[-\w]+)/(?P<pk>\d+)/$', views.creativity_detail, name="CreativityPage"),
]
