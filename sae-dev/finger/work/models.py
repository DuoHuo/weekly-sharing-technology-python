# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from util.models import MyModel
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class JianzhiRegion(MyModel):
    name = models.CharField(max_length=50, verbose_name=_("名字"))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('区域')
        verbose_name_plural = _('区域')

class JianzhiCategory(MyModel):
    name = models.CharField(max_length=50, verbose_name=_("名字"))
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('兼职分类')
        verbose_name_plural = _('兼职分类')

class Jianzhi(MyModel):
    type = models.ForeignKey(JianzhiCategory, blank=True, null=True, verbose_name=_("分类"))
    name = models.CharField(max_length=50,verbose_name=_("名字"))
    cover = models.URLField(blank=True, null=True,verbose_name=_("封面"))
    #description = models.TextField(max_length=500)
    company_name = models.CharField(max_length=100,verbose_name=_("公司名字"))
    number = models.CharField(max_length=50,verbose_name=_("人数"))
    expire_time = models.CharField(max_length=50,verbose_name=_("过期时间"))
    price = models.CharField(max_length=50,verbose_name=_("价格"))
    area = models.CharField(max_length=100,verbose_name=_("地址"))
    phone = models.CharField(max_length=20,verbose_name=_("电话"))
    content = models.TextField(max_length=500, blank=True, null=True,verbose_name=_("描述"))
    region = models.ForeignKey(JianzhiRegion,verbose_name=_("区域"))

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('兼职')
        verbose_name_plural = _('兼职')

class ApplicationJianzhi(MyModel):
    name = models.CharField(max_length=50,verbose_name=_("名字"))
    phone = models.CharField(max_length=20,verbose_name=_("电话"))
    work = models.ForeignKey(Jianzhi,verbose_name=_("工作"))
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('申请兼职')
        verbose_name_plural = _('申请兼职')


class AdvertiseJianzhi(MyModel):
    name = models.CharField(max_length=50, verbose_name=_("名字"))
    content = models.CharField(max_length=200, blank=True, null=True,verbose_name=_("内容"))
    cover = models.URLField(blank=True, null=True,verbose_name=_("封面"))
    class Meta:
        verbose_name = _('广告')
        verbose_name_plural = _('广告')




