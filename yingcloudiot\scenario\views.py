from django.shortcuts import render
from .models import Scenario,Collection,DevLink,CtrlSetting,LinkCtrlChannel,CtrlChannelParam
from .serializers import ScenarioSerializer,CollectionSerializer,DevLinkSerializer,CtrlSettingSerializer,\
LinkCtrlChannelSerializer,CtrlChannelParamSerializer
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

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class ScenarioViewSet(viewsets.ModelViewSet):
    """
    list:
    查询应用场景列表

    create:
    创建应用场景

    retrieve:
    查询应用场景详情

    update:
    更新应用场景

    partial_update:
    更新应用场景部分属性

    destroy:
    删除应用场景

    """

    serializer_class = ScenarioSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = Scenario.objects.all()

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)

    def list(self, request,):

        queryset = Scenario.objects.filter(owner=request.user)

        self.check_object_permissions(request,Scenario)
        serializer = ScenarioSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Scenario.objects.filter(owner=request.user)
        queryset_tmp = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(request,Scenario)
        serializer = ScenarioSerializer(queryset_tmp)
        return Response(serializer.data)


class CollectionViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备组合列表

    create:
    创建设备组合

    retrieve:
    查询设备组合详情

    update:
    更新设备组合

    partial_update:
    更新设备组合部分属性

    destroy:
    删除设备组合

    """	

    serializer_class = CollectionSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = Collection.objects.all()
           
    def list(self, request, scenarios_pk=None):
        queryset = Collection.objects.filter(scenario=scenarios_pk)
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None,scenarios_pk=None):
        queryset = Collection.objects.filter(pk=pk, scenario=scenarios_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = CollectionSerializer(queryset_tmp)
        return Response(serializer.data)

class DevLinkViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备组合关联设备列表

    create:
    创建设备组合关联设备

    retrieve:
    查询设备组合关联设备详情

    update:
    更新设备组合关联设备

    partial_update:
    更新设备组合关联设备部分属性

    destroy:
    删除设备组合关联设备

    """

    serializer_class = DevLinkSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = DevLink.objects.all()
           
    def list(self, request, scenarios_pk=None,collections_pk=None):
        queryset = DevLink.objects.filter(collection=collections_pk)
        # serializer = DevLinkSerializer(queryset, many=True)
        # return Response(serializer.data)
        tmplist = []
        for dl in queryset:
            tmplist.append({"device_id":dl.device.id,"device_title":dl.device.title,"devlink_id":dl.id})
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None, scenarios_pk=None,collections_pk=None):
        queryset = DevLink.objects.filter(pk=pk,collection=collections_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = DevLinkSerializer(queryset_tmp)
        return Response(serializer.data)



class CtrlSettingViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备组合设置列表

    create:
    创建设备组合设置

    retrieve:
    查询设备组合设置详情

    update:
    更新设备组合设置

    partial_update:
    更新设备组合设置部分属性

    destroy:
    删除设备组合设置

    """

    serializer_class = CtrlSettingSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = CtrlSetting.objects.all()
           
    def list(self, request, scenarios_pk=None,collections_pk=None):
        queryset = CtrlSetting.objects.filter(collection=collections_pk)
        serializer = CtrlSettingSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, scenarios_pk=None,collections_pk=None):
        queryset = CtrlSetting.objects.filter(pk=pk,collection=collections_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = CtrlSettingSerializer(queryset_tmp)
        return Response(serializer.data)



class LinkCtrlChannelViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备组合设置与控制通道关联列表

    create:
    创建设备组合设置与控制通道关联

    retrieve:
    查询设备组合设置与控制通道关联详情

    update:
    更新设备组合设置与控制通道关联

    partial_update:
    更新设备组合设置与控制通道关联部分属性

    destroy:
    删除设备组合设置与控制通道关联

    """

    serializer_class = LinkCtrlChannelSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = LinkCtrlChannel.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request,):

        queryset = LinkCtrlChannel.objects.filter(owner=request.user)

        # self.check_object_permissions(request,LinkCtrlChannel)
        # serializer = LinkCtrlChannelSerializer(queryset, many=True)
        # return Response(serializer.data)
        tmplist = []
        for dl in queryset:
            tmplist.append({"id":dl.id,"device_id":dl.ctrlchannel.device.id,"device_title":dl.ctrlchannel.device.title,"channel_id":dl.ctrlchannel.id,"channel_datatype":dl.ctrlchannel.datatype,"channel_title":dl.ctrlchannel.title,"setting_id":dl.ctrlsetting.id,"channel_title":dl.ctrlchannel.title,"setting_title":dl.ctrlsetting.title,"collection_id":dl.ctrlsetting.collection.id})
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None):
        queryset = LinkCtrlChannel.objects.filter(owner=request.user)
        queryset_tmp = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(request,LinkCtrlChannel)
        serializer = LinkCtrlChannelSerializer(queryset_tmp)
        return Response(serializer.data)


class CtrlChannelParamViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备组合下控制通道设置参数列表

    create:
    创建设备组合下控制通道设置参数

    retrieve:
    查询设备组合下控制通道设置参数详情

    update:
    更新设备组合下控制通道设置参数

    partial_update:
    更新设备组合下控制通道设置参数部分属性

    destroy:
    删除设备组合下控制通道设置参数

    """

    serializer_class = CtrlChannelParamSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = CtrlChannelParam.objects.all()
           
    def list(self, request, linkctrlchannels_pk=None):
        queryset = CtrlChannelParam.objects.filter(linkctrlchannel=linkctrlchannels_pk)
        serializer = CtrlChannelParamSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None,linkctrlchannels_pk=None):
        queryset = CtrlChannelParam.objects.filter(pk=pk, linkctrlchannel=linkctrlchannels_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = CtrlChannelParamSerializer(queryset_tmp)
        return Response(serializer.data)
