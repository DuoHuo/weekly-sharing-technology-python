# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.auth.models import User

class MyModel(models.Model):
    '''
    base class for all model
    '''
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    @classmethod
    def get_acitve_queryset(cls):
        return cls.objects.filter(is_active=True)

    class Meta:
        abstract = True