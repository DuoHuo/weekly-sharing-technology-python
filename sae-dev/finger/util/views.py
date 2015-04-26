# -*- coding:utf-8 -*-
from rest_framework import status, exceptions
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response
from json.encoder import JSONEncoder
import datetime
import json
from rest_framework import serializers
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

class MyFilterMixin(object):
    '''created by yilin 2014-6-11
       GikooModel basic list view mixin'''
    def gikooBasicFilter(self, queryset):
        return queryset.filter(is_active=True)


    def filter_ct(self,queryset):
        '''create_time'''
        now = datetime.datetime.now()
        create_time = self.request.QUERY_PARAMS.get('ct', None)
        if create_time is not None:
            queryset = queryset.filter(create_time__range=[now-timedelta(days=int(create_time)), now])
        return queryset

    def filter_ut(self,queryset):
        '''last_update_time'''
        now = datetime.datetime.now()
        last_update_time = self.request.QUERY_PARAMS.get('ut', None)
        if last_update_time is not None:
            queryset = queryset.filter(last_update_time__range=[now-timedelta(days=int(last_update_time)), now])

        ut_begin = self.request.QUERY_PARAMS.get('ut_begin', None)
        ut_end = self.request.QUERY_PARAMS.get('ut_end', None)
        if ut_begin != None and ut_end != None:
            if begin_end_time_input_check(ut_begin, ut_end):
                queryset = queryset.filter(Q(last_update_time__lte=ut_end)&Q(last_update_time__gte=ut_begin))
        return queryset

    def filter_q(self,queryset):
        '''q(contain_fields)'''
        key = self.request.QUERY_PARAMS.get('q', None)
        if key is not None and hasattr(self,'contain_fields') and self.contain_fields:
            qs = None
            for i in self.contain_fields:
                if qs is None:
                    qs = Q(**{'%s__icontains'%i: key})
                else:
                    qs = qs|Q(**{'%s__icontains'%i: key})

            if qs is not None:
                queryset = queryset.filter(qs)
        return queryset

    def filter_datetime(self,queryset):
        '''year,month(datetime_field)'''
        datetime_field = 'create_time'   #default field is create_time
        if hasattr(self,'datetime_field'):
            datetime_field = self.datetime_field
        if datetime_field is not None:
            year_field = self.request.QUERY_PARAMS.get('year', None)
            if year_field is not None:
                queryset = queryset.filter(**{'%s__year' %datetime_field:year_field})
            month_field = self.request.QUERY_PARAMS.get('month', None)
            if month_field is not None:
                queryset = queryset.filter(**{'%s__month' %datetime_field:month_field})
        return queryset

    def filter_fields_by_params(self,queryset):
        '''parameter to field(param_fields) yilin@2014-6-30
           e.g. define in your view:
               param_fields = (('task','task_id'),)
               http://url/?task=512, => queryset.filter(task_id=512)
        '''
        if hasattr(self,'param_fields') and self.param_fields:
            for param_name, field_name in self.param_fields:
                param_val = self.request.QUERY_PARAMS.get(param_name, None)
                if param_val is not None:
                    queryset = queryset.filter(**{field_name:param_val})
        return queryset

    def order_by(self,queryset, default='-id'):
        order_by = self.request.QUERY_PARAMS.get('order', default)
        #fix bug of usertask create_time is same, but section order show is wrong
        if order_by == "create_time":
            order_by = "id"
        elif order_by == "-create_time":
            order_by = "-id"
        queryset = queryset.order_by(order_by)
        return queryset

    def gikooQuery(self, queryset):
        '''更灵活的通用gikooQuery方法，子View中可以重写相应的方法自定义搜索逻辑 yilin@2014-6-30'''
        queryset = self.filter_ct(queryset)
        queryset = self.filter_ut(queryset)
        queryset = self.filter_q(queryset)
        queryset = self.filter_datetime(queryset)
        queryset = self.filter_fields_by_params(queryset)
        queryset = self.order_by(queryset)

        return queryset

class MyListAPIView(ListAPIView, MyFilterMixin):

    def get_queryset(self):
        u'''re-implement get query set '''
        #=======================================================================
        # if queryset = super(GikooListAPIView, self).get_queryset() == select * from model ??
        #  super(GikooListAPIView, self).get_queryset() replace with self.model.objects.filter
        #=======================================================================
        queryset = super(MyListAPIView, self).get_queryset()
        queryset = self.gikooBasicFilter(queryset)
        queryset = self.gikooQuery(queryset)
        return queryset

class MyListCreateAPIView(ListCreateAPIView, MyFilterMixin):
    u'''
         重新实现获得对象的全部列表
    super_user可以全部获得
         其他用户需要检查company 和 is_active
    '''
    def get_queryset(self):

        u'''re-implement get query set '''
        queryset = super(MyListCreateAPIView, self).get_queryset()
        queryset = self.gikooBasicFilter(queryset)
        queryset = self.gikooQuery(queryset)

        return queryset

class MyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    '''an APIView that support retrieve, update and delete an object, but that delete
        only set object inactive if the object has attribute named is_active'''

    def get_object(self):
        obj = super(MyRetrieveUpdateDestroyAPIView, self).get_object()
        if hasattr(obj, "is_active"):
            if obj.is_active:
                return obj
            else:
                raise Http404
        else:
            return obj

    # def destroy(self, request, *args, **kwargs):
    #     '''
    #     set an object inactive or remove it from DB
    #     '''
    #     obj = self.get_object()
    #     if(hasattr(obj, 'is_active')):
    #         setattr(obj, 'is_active', False)
    #         obj.save()
    #     else:
    #         obj.delete()
    #     try:
    #         c_id = ContentType.objects.get_for_model(obj).id
    #         r = Record.objects.get(content_type__pk=c_id,
    #           object_id=obj.id)
    #         r.is_active = False
    #         r.save()
    #     except Exception, e:
    #         print e
    #         pass
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

#自定义回复，http code固定200，用自定义code来区分出错情况或者成功
def generalJsonResponse(code, detail=None):
    return HttpResponse(JSONRenderer().render(generalResponseData(code, detail)),
      content_type="application/json")

def generalResponseData(code, detail=None):

    def get_error_detail(error_code):
        try:
            return ErrorCode.MSG[error_code]
        except KeyError:
            return 'Unknown error code(%d)' % error_code

    class GeneralResponse(object):
        def __init__(self, code, detail):
            self.code = code
            self.detail = detail

    class GeneralResponseSerializer(serializers.Serializer):
        code = serializers.IntegerField()
        detail = serializers.CharField(max_length=200)

    if detail is None:
        detail = get_error_detail(code)

    serializer = GeneralResponseSerializer(GeneralResponse(code, detail))
    return serializer.data

class ErrorCode(object):
    SUCCESS = 0
    FAILURE = 1
    AUTHENTICATION_FAIL = 4000
    INVALID_INPUT = 4001
    INTERNAL_ERROR = 4002
    EXISTED = 4003
    NOT_EXISTED = 4004
    ORIGIN_PSW_WRONG = 4005
    TRADE_NOT_SUFFICIENT = 4100
    MSG = {
        SUCCESS: 'Success',
        FAILURE: 'General failure',
        AUTHENTICATION_FAIL: 'Authenication failure',
        INVALID_INPUT: 'Invalid input',
        INTERNAL_ERROR: 'Internal Error',
        EXISTED: "Has existed",
        NOT_EXISTED: "Not existed",
        ORIGIN_PSW_WRONG: "original password wrong",
        TRADE_NOT_SUFFICIENT:"余额不足，请充值。",
    }