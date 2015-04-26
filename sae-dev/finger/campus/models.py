# -*- coding:utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from util.models import MyModel
from django.utils.translation import ugettext_lazy as _

class ReadCategory(MyModel):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("名字"))
    cover = models.URLField(blank=True, null=True, verbose_name=_("封面"))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('校园精读分类')
        verbose_name_plural = _('校园精读分类')

class Read(MyModel):
    type = models.ForeignKey(ReadCategory, blank=True, null=True,verbose_name=_("分类"))
    title = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("标题"))
    content = models.CharField(max_length=200, blank=True, null=True,verbose_name=_("内容"))
    introduction = models.CharField(max_length=200, blank=True, null=True,verbose_name=_("介绍"))
    cover = models.URLField(blank=True, null=True,verbose_name=_("封面"))

    class Meta:
        verbose_name = _('校园精读')
        verbose_name_plural = _('校园精读')

class ActivityCategory(MyModel):
    name = models.CharField(max_length=50, blank=True, null=True,verbose_name=_("名字"))
    cover = models.URLField(blank=True, null=True, verbose_name=_("封面"))

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('活动分类')
        verbose_name_plural = _('活动分类')

class Activity(MyModel):
    type = models.ForeignKey(ActivityCategory, blank=True, null=True,verbose_name=_("分类"))
    title = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("标题"))
    content = models.CharField(max_length=200, blank=True, null=True,verbose_name=_("内容"))
    introduction = models.CharField(max_length=200, blank=True, null=True,verbose_name=_("介绍"))
    cover = models.URLField(blank=True, null=True,verbose_name=_("封面"))

    class Meta:
        verbose_name = _('活动')
        verbose_name_plural = _('活动')

class ExamCategory(MyModel):
    name = models.CharField(max_length=50, blank=True, null=True,verbose_name=_("名字"))
    cover = models.URLField(blank=True, null=True, verbose_name=_("封面"))

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('考试分类')
        verbose_name_plural = _('考试分类')

class Exam(MyModel):
    type = models.ForeignKey(ExamCategory, null=True, blank=True,verbose_name=_("分类"))
    title = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("标题"))
    content = models.CharField(max_length=200, blank=True, null=True,verbose_name=_("内容"))
    introduction = models.CharField(max_length=200, blank=True, null=True,verbose_name=_("介绍"))
    cover = models.URLField(blank=True, null=True,verbose_name=_("封面"))
    class Meta:
        verbose_name = _('考试')
        verbose_name_plural = _('考试')

class SchoolInfoCategory(MyModel):
    name = models.CharField(max_length=50, blank=True, null=True,verbose_name=_("名字"))
    cover = models.URLField(blank=True, null=True, verbose_name=_("封面"))

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('信息分类')
        verbose_name_plural = _('信息分类')

class SchoolInfo(MyModel):
    type = models.ForeignKey(SchoolInfoCategory, null=True, blank=True,verbose_name=_("分类"))
    title = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("标题"))
    content = models.CharField(max_length=200, blank=True, null=True,verbose_name=_("内容"))
    introduction = models.CharField(max_length=200, blank=True, null=True,verbose_name=_("介绍"))
    cover = models.URLField(blank=True, null=True,verbose_name=_("封面"))
    date = models.CharField(blank=True, null=True, max_length=50, verbose_name=_("日期"))
    class Meta:
        verbose_name = _('信息')
        verbose_name_plural = _('信息')
