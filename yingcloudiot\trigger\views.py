from django.shortcuts import render
from .models import GlobalHttpAction,HttpKeyvalue,TriggerjobNew,TriggerjobNewMqtt
from .serializers import TriggerjobNewSerializer,TriggerjobNewMqttSerializer

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

from rest_framework_simplejwt.tokens import AccessToken
import urllib.parse
import urllib.request
import json

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


from rest_framework.decorators import api_view

@api_view()
def testglobalhttpaction(request, pk=None):
    try:
        act = GlobalHttpAction.objects.get(pk=pk)
        #queryset_tmp = get_object_or_404(queryset, pk=pk)
        url = act.url
        keyvalue = HttpKeyvalue.objects.filter(action=act)
        #keyvalue可能是字典，也可能是列表
        paras_data = {}
        for paras_tmp in keyvalue:
            paras_data[paras_tmp.key] = paras_tmp.value

        tokentmp = AccessToken()
        tokentmp = tokentmp.for_user(user=request.user)
        #print("004")
        token = 'Bearer'+' '+str(tokentmp)
        #print("003")
        headers = {'Authorization':token}
        #print(headers)

        data = urllib.parse.urlencode(paras_data).encode('utf-8')
        req=urllib.request.Request(url=url,data=data,headers=headers,method ='POST')
    except:
        info = {"status":"没有该动作"}
        return JSONResponse(info) 
    try:
        response = urllib.request.urlopen(req)
        if response:
            info = {"status":"GOOD"}
            return JSONResponse(info)
    except:
        info = {"status":"BAD"}
        return JSONResponse(info)    


class TriggerjobNewViewSet(viewsets.ModelViewSet):
    """
    list:
    查询触发HTTP任务列表

    create:
    创建触发HTTP任务

    retrieve:
    查询触发HTTP任务详情

    update:
    更新触发HTTP任务

    partial_update:
    更新触发HTTP任务部分属性

    destroy:
    删除触发HTTP任务

    """

    serializer_class = TriggerjobNewSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = TriggerjobNew.objects.all()

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)

    def list(self, request,):

        queryset = TriggerjobNew.objects.filter(owner=request.user)

        # self.check_object_permissions(request,Triggerjob)
        # serializer = TriggerjobNewSerializer(queryset, many=True)
        # return Response(serializer.data)

        tmplist = []
        for dl in queryset:
            tmplist.append({'id':dl.id,'title':dl.title,'owner':dl.owner.id,'device':dl.datachannel.device.title,'datachannel':dl.datachannel.id,'datachannel_title':dl.datachannel.title,'threshold_value':dl.threshold_value,'maximum':dl.maximum,'minimum':dl.minimum,'action':dl.action.id,'action_title':dl.action.title,'created':dl.created,'updated':dl.updated,'compare_choice':dl.compare_choice,'status_choice':dl.status_choice})
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None):
        queryset = TriggerjobNew.objects.filter(owner=request.user)
        queryset_tmp = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(request,Triggerjob)
        owner = str(queryset_tmp.owner.username)
        datachannel = queryset_tmp.datachannel
        threshold_value = queryset_tmp.threshold_value
        maximum = queryset_tmp.maximum
        minimum = queryset_tmp.minimum
        action = queryset_tmp.action
        created = queryset_tmp.created
        updated = queryset_tmp.updated
        compare_choice = queryset_tmp.compare_choice
        #serializer = TriggerjobSerializer(queryset_tmp)
        #return Response(serializer.data)
        info = {'id':queryset_tmp.id,'title':queryset_tmp.title,'owner':owner,'device':datachannel.device.title,'datachannel':datachannel.id,'datachannel_title':datachannel.title,'threshold_value':threshold_value,'maximum':maximum,'minimum':minimum,'action':action.id,'action_title':action.title,'created':created,'updated':updated,'compare_choice':compare_choice,'status_choice':queryset_tmp.status_choice}
        return JSONResponse(info)


class TriggerjobNewMqttViewSet(viewsets.ModelViewSet):
    """
    list:
    查询触发任务列表

    create:
    创建触发任务

    retrieve:
    查询触发任务详情

    update:
    更新触发任务

    partial_update:
    更新触发任务部分属性

    destroy:
    删除触发任务

    """

    serializer_class = TriggerjobNewMqttSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = TriggerjobNewMqtt.objects.all()

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)

    def list(self, request,):

        queryset = TriggerjobNewMqtt.objects.filter(owner=request.user)

        # self.check_object_permissions(request,Triggerjob)
        # serializer = TriggerjobNewSerializer(queryset, many=True)
        # return Response(serializer.data)

        tmplist = []
        for dl in queryset:
            tmplist.append({'id':dl.id,'title':dl.title,'owner':dl.owner.id,'device':dl.datachannel.device.title,'datachannel':dl.datachannel.id,'datachannel_title':dl.datachannel.title,'threshold_value':dl.threshold_value,'maximum':dl.maximum,'minimum':dl.minimum,'action':dl.action.id,'action_title':dl.action.title,'created':dl.created,'updated':dl.updated,'compare_choice':dl.compare_choice,'status_choice':dl.status_choice})
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None):
        queryset = TriggerjobNewMqtt.objects.filter(owner=request.user)
        queryset_tmp = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(request,Triggerjob)
        owner = str(queryset_tmp.owner.username)
        datachannel = queryset_tmp.datachannel
        threshold_value = queryset_tmp.threshold_value
        maximum = queryset_tmp.maximum
        minimum = queryset_tmp.minimum
        action = queryset_tmp.action
        created = queryset_tmp.created
        updated = queryset_tmp.updated
        compare_choice = queryset_tmp.compare_choice
        #serializer = TriggerjobSerializer(queryset_tmp)
        #return Response(serializer.data)
        info = {'id':queryset_tmp.id,'title':queryset_tmp.title,'owner':owner,'device':datachannel.device.title,'datachannel':datachannel.id,'datachannel_title':datachannel.title,'threshold_value':threshold_value,'maximum':maximum,'minimum':minimum,'action':action.id,'action_title':action.title,'created':created,'updated':updated,'compare_choice':compare_choice,'status_choice':queryset_tmp.status_choice}
        return JSONResponse(info)

