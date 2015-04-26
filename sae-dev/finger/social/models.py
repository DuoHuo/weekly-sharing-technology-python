# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from util.models import MyModel
from django.utils.translation import ugettext_lazy as _


class UserEx(MyModel):
    #关联的用户
    user = models.OneToOneField(User, verbose_name=_("用户"))
    #性别 True 男人
    gender = models.BooleanField(default=True, verbose_name=_("性别"))
    icon = models.URLField(null=True, blank=True, verbose_name=_("头像"))
    #用户积分
    credit = models.PositiveIntegerField(default=0, verbose_name=_("信用"))
    money = models.PositiveIntegerField(default=0, verbose_name=_("积分"))
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name=_("电话"))
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("地址"))
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("qq"))
    LEVEL_CHOICES = ((0, '大一'), (1, '大二'), (2, '大三'), (3, '大四'), (4,'研一'), (5, '研二'))
    level = models.PositiveIntegerField(default=0, choices=LEVEL_CHOICES, verbose_name=_("年级"))
    open_id = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name=_("唯一标示"))
    school = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("学校"))

    def __unicode__(self):
        return u'wechat user'

    class Meta:
        verbose_name = _('用户')
        verbose_name_plural = _('用户')

class ShopCategory(MyModel):
    name = models.CharField(max_length=50, verbose_name=_("名字"))
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('商店分类')
        verbose_name_plural = _('商店分类')

class WorkCategory(MyModel):
    name = models.CharField(max_length=50, verbose_name=_("名字"))
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('兼职分类')
        verbose_name_plural = _('兼职分类')


class Region(MyModel):
    name = models.CharField(max_length=50, verbose_name=_("名字"))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('区域')
        verbose_name_plural = _('区域')

class Shop(MyModel):
    type = models.ForeignKey(ShopCategory, verbose_name=_("分类"))
    cover = models.URLField(blank=True, null=True, verbose_name=_("封面"))
    name = models.CharField(max_length=50, verbose_name=_("名字"))
    description = models.TextField(max_length=500,verbose_name=_("描述"))
    introduction = models.CharField(max_length=100, verbose_name=_("介绍"))
    phone = models.CharField(max_length=20, blank=True, null=True,verbose_name=_("电话"))
    location = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("地址"))
    region = models.ForeignKey(Region, verbose_name=_("区域"))
    class Meta:
        verbose_name = _('商店')
        verbose_name_plural = _('商店')


class Work(MyModel):
    type = models.ForeignKey(WorkCategory, blank=True, null=True, verbose_name=_("分类"))
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
    region = models.ForeignKey(Region,verbose_name=_("区域"))

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('兼职')
        verbose_name_plural = _('兼职')

class ApplicationWork(MyModel):
    name = models.CharField(max_length=50,verbose_name=_("名字"))
    phone = models.CharField(max_length=20,verbose_name=_("电话"))
    work = models.ForeignKey(Work,verbose_name=_("工作"))
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('申请兼职')
        verbose_name_plural = _('申请兼职')

class AdvertiseCategory(MyModel):
    name = models.CharField(max_length=50,verbose_name=_("名字"))
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('广告分类')
        verbose_name_plural = _('广告分类')

class Advertise(MyModel):
    type = models.ForeignKey(AdvertiseCategory, blank=True, null=True,verbose_name=_("分类"))
    name = models.CharField(max_length=50, verbose_name=_("名字"))
    content = models.CharField(max_length=200, blank=True, null=True,verbose_name=_("内容"))
    cover = models.URLField(blank=True, null=True,verbose_name=_("封面"))
    class Meta:
        verbose_name = _('广告')
        verbose_name_plural = _('广告')

