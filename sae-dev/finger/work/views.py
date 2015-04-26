# -*- coding:utf-8 -*-
from util.views import generalJsonResponse
from util.views import MyListAPIView, MyListCreateAPIView, MyRetrieveUpdateDestroyAPIView
from models import *# Create your views here.


class ListRegion(MyListCreateAPIView):
    model = JianzhiRegion
    permission_classes = ()

class ListWorkCategory(MyListCreateAPIView):
    model = JianzhiCategory
    permission_classes = ()


class ListWork(MyListCreateAPIView):
    model = Jianzhi
    permission_classes = ()
    param_fields = (('type','type_id'), ('region', 'region_id'))

class WorkDetail(MyRetrieveUpdateDestroyAPIView):
    model = Jianzhi
    permission_classes = ()

class ListAdvertise(MyListCreateAPIView):
    model = AdvertiseJianzhi
    permission_classes = ()

class ApplyWork(MyListCreateAPIView):
    model = ApplicationJianzhi
    permission_classes = ()
    authentication_classes = ()