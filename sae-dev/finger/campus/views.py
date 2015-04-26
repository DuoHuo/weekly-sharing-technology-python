# -*- coding:utf-8 -*-
# import serializers
from rest_framework.response import Response
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from util.views import generalJsonResponse
from util.views import MyListAPIView, MyListCreateAPIView, MyRetrieveUpdateDestroyAPIView
from models import *
import requests
import re

class ListRead(MyListCreateAPIView):
    model = Read
    permission_classes = ()
    param_fields = (('type','type_id'),)

class ListActivity(MyListCreateAPIView):
    model = Activity
    permission_classes = ()
    param_fields = (('type','type_id'),)

class ListExam(MyListCreateAPIView):
    model = Exam
    permission_classes = ()
    param_fields = (('type','type_id'),)

class ListSchoolInfo(MyListCreateAPIView):
    model = SchoolInfo
    permission_classes = ()
    param_fields = (('type','type_id'),)

class ListReadCategory(MyListCreateAPIView):
    model = ReadCategory
    permission_classes = ()

class ListActivityCategory(MyListCreateAPIView):
    model = ActivityCategory
    permission_classes = ()

class ListExamCategory(MyListCreateAPIView):
    model = ExamCategory
    permission_classes = ()

class ListSchoolInfoCategory(MyListCreateAPIView):
    model = SchoolInfoCategory
    permission_classes = ()


def search_book(request):
    data = {}
    text = request.GET.get('text', None)
    if text:
        r = requests.get('http://lib2.nuist.edu.cn/opac/openlink.php?strSearchType=title&match_flag=forward&historyCount=1\
            &strText=%s&doctype=ALL&displaypg=200&showmode=list&sort=CATA_DATE&orderby=desc&dept=ALL' %text)
        # print r.content
        match = re.compile(r'<a href="item.php\?marc_no=(\d+)" >(.*)</a>')
        book_list = re.findall(match,r.content)
        # print book_list
        data['results'] = book_list
        data['status'] = True
    else:
        data['status'] = False
    print data
    response = HttpResponse(content=json.dumps(data), content_type='application/json')
    return response

def book_detail(request, id):
    data = {}
    r = requests.get('http://lib2.nuist.edu.cn/opac/item.php?marc_no=%s'%id)
    match0 = re.compile(r'<dt>(.*)</dt>')
    match1 = re.compile(r'<dd>(.*)</dd>')
    match2 = re.compile(r'<td  width="25%" title="(.*)"><img src="../tpl/images/place_marker.gif" />(.*)</td>')
    match3 = re.compile(r'<td  width="20%" >(.*)</td>')

    dt = re.findall(match0,r.content)
    dd = re.findall(match1,r.content)
    address = re.findall(match2,r.content)
    flag = re.findall(match3,r.content)
    data['status'] = True
    data['dt'] = dt
    data['dd'] = dd
    data['address'] = address
    data['flag'] = flag
    response = HttpResponse(content=json.dumps(data), content_type='application/json')
    return response



