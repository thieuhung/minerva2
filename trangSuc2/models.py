# Create your models here.
from django.db import models
from django.shortcuts import render
from django.db.models.query import QuerySet
from pprint import PrettyPrinter
# from __future__ import unicode_literals
from django.db.models.functions import Trim

class trangSuc(models.Model):
    loai = models.TextField()
    nhom = models.TextField()
    ten = models.TextField()
    gia = models.TextField()
    thongTinSP = models.TextField()
    hinh = models.TextField()
    boSuuTap = models.TextField(null=True,blank=True)
    loaiDaChinh = models.TextField(null=True,blank=True)
    mauDaChinh = models.TextField(null=True,blank=True)
    hinhDangDa = models.TextField(null=True,blank=True)

    def clean(self):
        for field in self._meta.fields:
            if isinstance(field, (models.CharField, models.TextField)):
                setattr(self, field.name, getattr(self, field.name).strip())

    class Meta:
        ordering = ('id',)

class Product(models.Model):
    productID = models.ForeignKey(trangSuc, on_delete=models.CASCADE)
    loai = models.TextField()
    nhom = models.TextField()
    ten = models.TextField()
    gia = models.TextField()
    thongTinSP = models.TextField()
    hinh = models.TextField()
    boSuuTap = models.TextField(null=True, blank=True)
    loaiDaChinh = models.TextField(null=True, blank=True)
    mauDaChinh = models.TextField(null=True, blank=True)
    hinhDangDa = models.TextField(null=True, blank=True)

