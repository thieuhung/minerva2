# Create your views here.
import os

import django
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render

from .models import trangSuc

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings");
django.setup()


# Create your views here.
def list_trangSuc(request):
    all_albums = trangSuc.objects.all()
    paginator = Paginator(all_albums, 20)
    pageNumber = request.GET.get('page')
    try:
        all_albums = paginator.page(pageNumber)
    except PageNotAnInteger:
        all_albums = paginator.page(1)
    except EmptyPage:
        all_albums = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'all_albums': all_albums})


def nhom(request, nhom_id=None, loai_id=None):
    try:
        if nhom_id == 'v':
            nhom_id = 'Trang sức vàng'
        elif nhom_id == 'b':
            nhom_id = 'Trang sức bạc'
        elif nhom_id == 'k':
            nhom_id = 'Kim cương'
        rsProduct = trangSuc.objects.filter(nhom__contains=nhom_id)
        if loai_id == '0':
            loai_id = 'Nhẫn'
        elif loai_id == '1':
            loai_id = 'Bông tai'
        elif loai_id == '2':
            loai_id = 'Dây chuyền'
        elif loai_id == '3':
            loai_id = 'Mặt dây chuyền'
        elif loai_id == '4':
            loai_id = 'Dây cổ'
        if loai_id != None:
            rsProduct = trangSuc.objects.filter(nhom__contains=nhom_id, loai__contains=loai_id)

    except rsProduct.DoesNotExist:
        raise Http404("Product does not exist")

    paginator = Paginator(rsProduct, 20)
    pageNumber = request.GET.get('page')
    try:
        rsProduct = paginator.page(pageNumber)
    except PageNotAnInteger:
        rsProduct = paginator.page(1)
    except EmptyPage:
        rsProduct = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'all_albums': rsProduct})


def product(request, product_id):
    try:
        rsProduct = trangSuc.objects.get(id=product_id)
    except rsProduct.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'product.html', {'album': rsProduct})
