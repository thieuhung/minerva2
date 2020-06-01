from django.conf.urls import url
from django.core.handlers.wsgi import WSGIRequest
from django.urls import path

from . import views
from trangSuc2 import views

app_name = 'trangSuc2'

urlpatterns = [
    path('trangSuc2', views.list_trangSuc),

    url(r'/index/', views.list_trangSuc, name='index'),
    url(r'^/product/(?P<product_id>[0-9]+)/$', views.product, name='product'),
    url(r'^/nhom/(?P<nhom_id>[b-v]+)/$', views.nhom, name='nhom'),
    url(r'^/nhom/(?P<nhom_id>[b-v]+)/loai/(?P<loai_id>[0-9])/$', views.nhom, name='nhom')

]
