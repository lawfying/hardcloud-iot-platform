from django.shortcuts import render
from django_celery_beat.models import IntervalSchedule,SolarSchedule,CrontabSchedule,PeriodicTask,ClockedSchedule
from .serializers_beat import IntervalScheduleSerializer,SolarScheduleSerializer,CrontabScheduleSerializer,PeriodicTaskSerializer,\
    ClockedScheduleSerializer,GlobalHttpActionSerializer,HttpKeyvalueSerializer,GlobalMqttActionSerializer,MqttKeyvalueSerializer,\
        IntervalScheduleTopSerializer,SolarScheduleTopSerializer,CrontabScheduleTopSerializer,PeriodicTaskTopSerializer,ClockedScheduleTopSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt import authentication
from rest_framework import permissions

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action
from rest_framework.decorators import detail_route, list_route


from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from datetime import datetime

from .models import GlobalHttpAction,HttpKeyvalue,GlobalMqttAction,MqttKeyvalue,\
    IntervalScheduleNew,CrontabScheduleNew,ClockedScheduleNew,PeriodicTaskNew

from django.db import models

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class IntervalScheduleViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询间隔时间计划列表

    create:
    创建间隔时间计划

    retrieve:
    查询间隔时间计划详情

    update:
    更新间隔时间计划

    partial_update:
    更新间隔时间计划部分属性

    destroy:
    删除间隔时间计划

    """

    serializer_class = IntervalScheduleSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = IntervalScheduleNew.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def list(self, request,):

        queryset = IntervalScheduleNew.objects.filter(owner=request.user)

        self.check_object_permissions(request,IntervalScheduleNew)
        serializer = IntervalScheduleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset_tmp = IntervalScheduleNew.objects.get(pk=pk)
        serializer = IntervalScheduleSerializer(queryset_tmp)
        return Response(serializer.data)

class ClockedScheduleViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询定时计划列表

    create:
    创建定时计划

    retrieve:
    查询定时计划详情

    update:
    更新定时计划

    partial_update:
    更新定时计划部分属性

    destroy:
    删除定时计划

    """

    serializer_class = ClockedScheduleSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = ClockedScheduleNew.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def list(self, request,):

        queryset = ClockedScheduleNew.objects.filter(owner=request.user)

        self.check_object_permissions(request,ClockedScheduleNew)
        serializer = ClockedScheduleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset_tmp = ClockedScheduleNew.objects.get(pk=pk)
        serializer = ClockedScheduleSerializer(queryset_tmp)
        return Response(serializer.data)

class SolarScheduleViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询太阳时计划列表

    create:
    创建太阳时计划

    retrieve:
    查询太阳时计划详情

    update:
    更新太阳时计划

    partial_update:
    更新太阳时计划部分属性

    destroy:
    删除太阳时计划

    """

    serializer_class = SolarScheduleSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = SolarSchedule.objects.all()


    def list(self, request,):

        queryset = SolarSchedule.objects.all()

        self.check_object_permissions(request,SolarSchedule)
        serializer = SolarScheduleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset_tmp = SolarSchedule.objects.get(pk=pk)
        serializer = SolarScheduleSerializer(queryset_tmp)
        return Response(serializer.data)


class CrontabScheduleViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询例行时间计划列表

    create:
    创建例行时间计划

    retrieve:
    查询例行时间计划详情

    update:
    更新例行时间计划

    partial_update:
    更新例行时间计划部分属性

    destroy:
    删除例行时间计划

    """

    serializer_class = CrontabScheduleSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = CrontabScheduleNew.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def list(self, request,):

        queryset = CrontabScheduleNew.objects.filter(owner=request.user)

        self.check_object_permissions(request,CrontabScheduleNew)
        serializer = CrontabScheduleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset_tmp = CrontabScheduleNew.objects.get(pk=pk)
        serializer = CrontabScheduleSerializer(queryset_tmp)
        return Response(serializer.data)


class PeriodicTaskViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询例行时间计划列表

    create:
    创建例行时间计划

    retrieve:
    查询例行时间计划详情

    update:
    更新例行时间计划

    partial_update:
    更新例行时间计划部分属性

    destroy:
    删除例行时间计划

    """

    serializer_class = PeriodicTaskSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = PeriodicTaskNew.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def list(self, request,):

        queryset = PeriodicTaskNew.objects.filter(owner=request.user)

        # self.check_object_permissions(request,PeriodicTask)
        # serializer = PeriodicTaskSerializer(queryset, many=True)
        # from celery import current_app
        # tasks = list(sorted(name for name in current_app.tasks
        #                     if not name.startswith('celery.')))
        # print(tasks)
        # return Response(serializer.data)
        tmplist = []
        
        for tk in queryset:
            scheduleplan = ''
            intervalid = ''
            cronid = ''
            clkid = ''
            #print(tk.interval)
            if tk.interval:
                int_sch = tk.interval
                scheduleplan = "每隔"+str(int_sch.every)+str(int_sch.period)
                intervalid = tk.interval.id
            elif tk.crontab:
                cron_sch = tk.crontab
                scheduleplan = cron_sch.minute+" "+cron_sch.hour+" "+cron_sch.day_of_week+" "+cron_sch.day_of_month+" "+cron_sch.month_of_year
                cronid = tk.crontab.id
            elif tk.clocked:
                clk_sch = tk.clocked
                scheduleplan = clk_sch.clocked_time
                clkid = tk.clocked.id
            else:
                scheduleplan = ''
                intervalid = ''
                cronid = ''
                clkid = ''

            import json
            tmpact = json.loads(tk.kwargs)
            print(tmpact.get('http_action'))
            #print(tmpact['action'])
            action_type = ''
            action_id = ''
            if tmpact.get('http_action'):
                gact = GlobalHttpAction.objects.get(pk=tmpact['http_action'])
                action_type = "HTTP"
                action_id = gact.id
            if tmpact.get('mqtt_action'):
                gact = GlobalMqttAction.objects.get(pk=tmpact['mqtt_action'])
                action_type = "MQTT"
                action_id = gact.id
            #print(gact.title)
            tmplist.append({"id":tk.id,"name":tk.name,"scheduleplan":scheduleplan,"action":gact.title,"action_type":action_type,"action_id":action_id,"interval":intervalid,"crontab":cronid,"clocked":clkid,\
                "expires":tk.expires,"start_time":tk.start_time,"enabled":tk.enabled,"total_run_count":tk.total_run_count,\
                    "description":tk.description,"last_run_at":tk.last_run_at})
        print(tmplist)
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None):
        queryset_tmp = PeriodicTaskNew.objects.get(pk=pk)
        serializer = PeriodicTaskSerializer(queryset_tmp)
        return Response(serializer.data)

# global action
class GlobalHttpActionViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询全局HTTP动作列表

    create:
    创建全局HTTP动作计划

    retrieve:
    查询全局HTTP动作详情

    update:
    更新全局HTTP动作

    partial_update:
    更新全局HTTP动作部分属性

    destroy:
    删除全局HTTP动作

    """

    serializer_class = GlobalHttpActionSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = GlobalHttpAction.objects.all()

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)


    def list(self, request,):

        queryset = GlobalHttpAction.objects.filter(owner=request.user)

        self.check_object_permissions(request,GlobalHttpAction)
        serializer = GlobalHttpActionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset_tmp = GlobalHttpAction.objects.get(pk=pk)
        serializer = GlobalHttpActionSerializer(queryset_tmp)
        return Response(serializer.data)

class HttpKeyvalueViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询HTTP动作参数列表

    create:
    创建HTTP动作参数

    retrieve:
    查询HTTP动作参数详情

    update:
    更新HTTP动作参数

    partial_update:
    更新HTTP动作参数部分属性

    destroy:
    删除HTTP动作参数

    """	

    serializer_class = HttpKeyvalueSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = HttpKeyvalue.objects.all()

           
    def list(self, request, globalhttpaction_pk=None):
        queryset = HttpKeyvalue.objects.filter(action=globalhttpaction_pk)
        serializer = HttpKeyvalueSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None,globalhttpaction_pk=None):
        queryset = HttpKeyvalue.objects.filter(pk=pk, action=globalhttpaction_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = HttpKeyvalueSerializer(queryset_tmp)
        return Response(serializer.data)

#mqtt action
# global action
class GlobalMqttActionViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询全局MQTT动作列表

    create:
    创建全局MQTT动作计划

    retrieve:
    查询全局MQTT动作详情

    update:
    更新全局MQTT动作

    partial_update:
    更新全局MQTT动作部分属性

    destroy:
    删除全局MQTT动作

    """

    serializer_class = GlobalMqttActionSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = GlobalMqttAction.objects.all()

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)


    def list(self, request,):

        queryset = GlobalMqttAction.objects.filter(owner=request.user)

        self.check_object_permissions(request,GlobalMqttAction)
        serializer = GlobalMqttActionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset_tmp = GlobalMqttAction.objects.get(pk=pk)
        serializer = GlobalMqttActionSerializer(queryset_tmp)
        return Response(serializer.data)

class MqttKeyvalueViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询MQTT动作参数列表

    create:
    创建MQTT动作参数

    retrieve:
    查询MQTT动作参数详情

    update:
    更新MQTT动作参数

    partial_update:
    更新MQTT动作参数部分属性

    destroy:
    删除MQTT动作参数

    """	

    serializer_class = MqttKeyvalueSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = MqttKeyvalue.objects.all()
           
    def list(self, request, globalmqttaction_pk=None):
        queryset = MqttKeyvalue.objects.filter(action=globalmqttaction_pk)
        serializer = MqttKeyvalueSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None,globalmqttaction_pk=None):
        queryset = MqttKeyvalue.objects.filter(pk=pk, action=globalmqttaction_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = MqttKeyvalueSerializer(queryset_tmp)
        return Response(serializer.data)


#for top 
class IntervalScheduleTopViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询间隔时间计划列表

    create:
    创建间隔时间计划

    retrieve:
    查询间隔时间计划详情

    update:
    更新间隔时间计划

    partial_update:
    更新间隔时间计划部分属性

    destroy:
    删除间隔时间计划

    """

    serializer_class = IntervalScheduleTopSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = IntervalSchedule.objects.all()


    def list(self, request,):

        queryset = IntervalSchedule.objects.all()

        self.check_object_permissions(request,IntervalSchedule)
        serializer = IntervalScheduleTopSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset_tmp = IntervalSchedule.objects.get(pk=pk)
        serializer = IntervalScheduleTopSerializer(queryset_tmp)
        return Response(serializer.data)

class SolarScheduleTopViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询太阳时计划列表

    create:
    创建太阳时计划

    retrieve:
    查询太阳时计划详情

    update:
    更新太阳时计划

    partial_update:
    更新太阳时计划部分属性

    destroy:
    删除太阳时计划

    """

    serializer_class = SolarScheduleTopSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = SolarSchedule.objects.all()


    def list(self, request,):

        queryset = SolarSchedule.objects.all()

        self.check_object_permissions(request,SolarSchedule)
        serializer = SolarScheduleTopSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset_tmp = SolarSchedule.objects.get(pk=pk)
        serializer = SolarScheduleTopSerializer(queryset_tmp)
        return Response(serializer.data)


class CrontabScheduleTopViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询例行时间计划列表

    create:
    创建例行时间计划

    retrieve:
    查询例行时间计划详情

    update:
    更新例行时间计划

    partial_update:
    更新例行时间计划部分属性

    destroy:
    删除例行时间计划

    """

    serializer_class = CrontabScheduleSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = CrontabSchedule.objects.all()


    def list(self, request,):

        queryset = CrontabSchedule.objects.all()

        self.check_object_permissions(request,CrontabSchedule)
        serializer = CrontabScheduleTopSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset_tmp = CrontabSchedule.objects.get(pk=pk)
        serializer = CrontabScheduleTopSerializer(queryset_tmp)
        return Response(serializer.data)


class ClockedScheduleTopViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询定时时间计划列表

    create:
    创建定时时间计划

    retrieve:
    查询定时时间计划详情

    update:
    更新定时时间计划

    partial_update:
    更新定时时间计划部分属性

    destroy:
    删除定时时间计划

    """

    serializer_class = ClockedScheduleTopSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = ClockedSchedule.objects.all()


    def list(self, request,):

        queryset = ClockedSchedule.objects.all()

        self.check_object_permissions(request,ClockedSchedule)
        serializer = ClockedScheduleTopSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset_tmp = ClockedSchedule.objects.get(pk=pk)
        serializer = ClockedScheduleTopSerializer(queryset_tmp)
        return Response(serializer.data)



class PeriodicTaskTopViewSet_Beat(viewsets.ModelViewSet):
    """
    list:
    查询例行时间计划列表

    create:
    创建例行时间计划

    retrieve:
    查询例行时间计划详情

    update:
    更新例行时间计划

    partial_update:
    更新例行时间计划部分属性

    destroy:
    删除例行时间计划

    """

    serializer_class = PeriodicTaskTopSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = PeriodicTask.objects.all()


    def list(self, request,):

        queryset = PeriodicTask.objects.all()

        self.check_object_permissions(request,PeriodicTask)
        serializer = PeriodicTaskTopSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset_tmp = PeriodicTask.objects.get(pk=pk)
        serializer = PeriodicTaskTopSerializer(queryset_tmp)
        return Response(serializer.data)