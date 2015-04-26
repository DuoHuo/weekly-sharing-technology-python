# Create your views here.
# -*- coding:utf-8 -*-
import serializers
from rest_framework.response import Response
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
# from util.misc import DateTimeJsonEncoder
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from util.views import generalJsonResponse
from util.views import MyListAPIView, MyListCreateAPIView, MyRetrieveUpdateDestroyAPIView
from models import *
from django.contrib.auth.models import AnonymousUser

import datetime
def send_email(name, phone):
    from sae.mail import EmailMessage
    m = EmailMessage()
    m.to = 'zhijiannanxin@sina.com'
    m.subject = ''
    m.html = 'name: %s\nphone: %s' %(name, phone)
    m.smtp = ('smtp.163.com', 25, 'zhangcr1992@163.com', 'password', 'zxc123')
    m.send()

class ListShop(MyListCreateAPIView):
    model = Shop
    permission_classes = ()
    param_fields = (('type','type_id'), ('region', 'region_id'))
    # filter_fields = ('type_id', 'region',)
    # serializer_class =
    contain_fields = ()

class ListRegion(MyListCreateAPIView):
    model = Region
    permission_classes = ()

class ShopDetail(MyRetrieveUpdateDestroyAPIView):
    model = Shop
    permission_classes = ()

class ListShopCategory(MyListCreateAPIView):
    model = ShopCategory
    permission_classes = ()

class ListWorkCategory(MyListCreateAPIView):
    model = WorkCategory
    permission_classes = ()

class ListWork(MyListCreateAPIView):
    model = Work
    permission_classes = ()
    param_fields = (('type','type_id'), ('region', 'region_id'))

class WorkDetail(MyRetrieveUpdateDestroyAPIView):
    model = Work
    permission_classes = ()

class ListAdvertise(MyListCreateAPIView):
    model = Advertise
    permission_classes = ()
    param_fields = (('type', 'type_id'),)

class ApplyWork(MyListCreateAPIView):
    model = ApplicationWork
    permission_classes = ()
    authentication_classes = ()


class ListUser(MyListCreateAPIView):
    model = UserEx
    serializer_class = serializers.UserExListSerializer
    permission_classes = ()

    def get_queryset(self):
        import pdb;pdb.set_trace()
        pass

class RetrieveUpdateDestroyUser(MyRetrieveUpdateDestroyAPIView):
    model = UserEx
    serializer_class = serializers.UserExDetailSerializer
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user is not None:
            user = self.request.user
            self.object = user.userex
            serializer = self.get_serializer(self.object)
            return Response(serializer.data)
        else:
            return Response("not found")

    def put(self, request, *args, **kwargs):
        res = super(RetrieveUpdateDestroyUser,self).put(request, *args, **kwargs)
        password = request.DATA.get('password', None)
        if password is not None:
            old_psw = request.DATA.get('old_password', None)
            if old_psw is not None:
                user = request.user
                if user.check_password(old_psw):
                    user.set_password(password)
                    user.save()
                    self.object.user.save()
                    return res
            return generalJsonResponse(4005)
        return res


def login_user(username, password, auth_method, request):
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        #返回用户信息
        try:
            ue = user.userex
        except ObjectDoesNotExist:
            gender = request.POST.get('gender', None)
            level = request.POST.get('level',None)
            info = {
                'user': user,
                'phone': request.POST.get('phone', None),
                'address': request.POST.get('address',None),
                'qq': request.POST.get('qq', None),
                'open_id': request.POST.get('open_id',None)
            }

            if gender is not None:
                info['gender'] = int(gender)
            if level is not None:
                info['level'] = int(level)

            ue = UserEx.objects.create(**info)
        data = serializers.UserExDetailSerializer(ue).data
        data['user'] = ue.user.id
        request.session['username'] = username
        print request.session['username']

        #针对client端
        if(auth_method == 'token'):
            tk = Token.objects.get_or_create(user=user)[0]
            data['token'] = tk.key
        #web端
        else:
            login(request, user)
            data['token'] = None
        return data
    return None



def check_username(request):
    data = {}
    username = request.GET.get('username',None)
    if username is not None:
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            data['valid'] = True
        else:
            data['valid'] = False
            data['message'] = 'the user is already registered'
    data['status'] = True
    response = HttpResponse(json.dumps(data), content_type="application/json")
    return response

def get_info(request):
    data = {}
    # username = request.session.get('username', None)
    # print username
    # import pdb;pdb.set_trace()
    # if username is not None:
    #     try:
    #         userex = UserEx.objects.get(user__username=username)
    #     except UserEx.DoesNotExist:
    #         data['valid'] = False
    #     else:
    #         data['valid'] = True
    #         data.update(
    #             {
    #                 'username':username,
    #                 'gender': userex.gender,
    #                 'phone': userex.phone,
    #                 'address': userex.address,
    #                 'level': userex.level,
    #                 'qq': userex.qq,
    #                 'school': userex.school,
    #                 # 'card_number': '%06d' %userex.id
    #
    #             })
    # request.user
    # import pdb;pdb.set_trace()
    if request.user.id !=None:
        userex = request.user.userex
        data['valid'] = True
        data.update(
            {
                'username':request.user.username,
                'gender': userex.gender,
                'phone': userex.phone,
                'address': userex.address,
                'level': userex.level,
                'qq': userex.qq,
                'school': userex.school,
                # 'card_number': '%06d' %userex.id

            })
    else:
        data['valid'] = False
    response = HttpResponse(json.dumps(data), content_type="application/json")
    return response

#注册 并登陆
class UserRegiter(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username',None).strip()
        password = request.POST.get('password', None).strip()
        auth_method = request.POST.get('auth',None)
        crypted = make_password(password)
        try:
            user = User.objects.create(username=username, password=crypted)
            data = login_user(username, password, auth_method, request)
            return generalJsonResponse(0, data)
        except Exception,e:
            print e
            return generalJsonResponse(1, e)


class UserLogin(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        #同一个url web端传username password,登录状态保存在session; client加传一个 auth=token，返回一个token字符串
        #所有调用均需要加传Authorization: Token [token值]作为身份凭证，logout之后token失效，否则一直有效。
        auth_method = request.POST.get('auth',None)
        username = request.POST.get('username',None)
        password = request.POST.get('password', None)
        #验证用户身份
        data = login_user(username, password, auth_method, request)
        if data is not None:
            return generalJsonResponse(0, detail=data)
        else:
            return generalJsonResponse(1)


class UserLogout(APIView):
    model = UserEx
    permission_classes = ()
    def post(self, request, *args, **kwargs):
        if(request.user is None):
            print 'token'
            tk = Token.objects.filter(key=request.auth())
            for i in tk:
                i.delete()
        else:
            print 'logout'
            logout(request)
            print request.user
        return generalJsonResponse(0)


# class OauthUserBind(APIView):
#     permission_classes = ()
#     model = UserBind
#
#     DEFAULT_PSW = 'hch911@irudong.com'
#
#     def post(self, request, *args, **kwargs):
#         psuid = request.DATA.get('psuid')
#         try:
#             ub = UserBind.objects.get(psuid=psuid)
#             user = ub.user
#         except Exception,e:
#             try:
#                 crypted = make_password(self.DEFAULT_PSW)
#                 user = User.objects.create(username=psuid, password=crypted)
#             except Exception,e:
#                 return generalJsonResponse(1, detail=e)
#             icon = request.DATA.get('icon')
#             nickname = request.DATA.get('nickname')
#             type = request.DATA.get('type')
#             nickname = nickname+'_'+type
#             try:
#                 ue = UserEx.objects.create(user=user, icon=icon, nickname=nickname)
#             except Exception,e:
#                 user.delete()
#                 return generalJsonResponse(1, detail=e)
#             accesstoken = request.DATA.get('accesstoken')
#             expiredtime = request.DATA.get('expiredtime')
#             try:
#                 ub = UserBind.objects.create(user=user, psuid=psuid,\
#                                              type=type, accesstoken=accesstoken, expiredtime=expiredtime)
#             except Exception,e:
#                 user.delete()
#                 ue.delete()
#                 return generalJsonResponse(1, detail=e)
#         auth_method = request.DATA.get('auth')
#         data = login_user(psuid, self.DEFAULT_PSW, auth_method, request)
#         return generalJsonResponse(0, detail=data)
