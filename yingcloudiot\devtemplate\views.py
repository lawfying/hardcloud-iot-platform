from django.shortcuts import render
from .models import DevTemplate,TemplateTags,TplDataChannel,TplDataUnit,TplCtrlChannel,TplCtrlUnit
from devtemplate.serializers import DevTemplateSerializer,TemplateTagsSerializer,TplDataChannelSerializer,\
TplDataUnitSerializer,TplCtrlChannelSerializer,TplCtrlUnitSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt import authentication
from rest_framework import permissions

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

class DevTemplateViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备模板列表

    create:
    创建设备模板

    retrieve:
    查询设备模板详情

    update:
    更新设备模板

    partial_update:
    更新设备模板部分属性

    destroy:
    删除设备模板

    """

    serializer_class = DevTemplateSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = DevTemplate.objects.all()

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)

    def list(self, request,):

        queryset = DevTemplate.objects.filter(owner=request.user).order_by('-created')

        self.check_object_permissions(request,DevTemplate)
        serializer = DevTemplateSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = DevTemplate.objects.filter(owner=request.user)
        queryset_tmp = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(request,DevTemplate)
        serializer = DevTemplateSerializer(queryset_tmp)
        return Response(serializer.data)

class TemplateTagsViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备模板标签列表

    create:
    创建设备模板标签

    retrieve:
    查询设备模板标签详情

    update:
    更新设备模板标签

    partial_update:
    更新设备模板标签部分属性

    destroy:
    删除设备模板标签

    """	

    serializer_class = TemplateTagsSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = TemplateTags.objects.all()
           
    def list(self, request, devtemplates_pk=None):
        queryset = TemplateTags.objects.filter(devtemplate=devtemplates_pk)
        serializer = TemplateTagsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None,devtemplates_pk=None):
        queryset = TemplateTags.objects.filter(pk=pk, devtemplate=devtemplates_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = CatTmpTagsSerializer(queryset_tmp)
        return Response(serializer.data)

class TplDataChannelViewSet(viewsets.ModelViewSet):
    """
    list:
    查询模板数据通道列表

    create:
    创建模板数据通道

    retrieve:
    查询模板数据通道详情

    update:
    更新模板数据通道

    partial_update:
    更新模板数据通道部分属性

    destroy:
    删除模板数据通道

    """
    serializer_class = TplDataChannelSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = TplDataChannel.objects.all()
           
    def list(self, request, devtemplates_pk=None):
        queryset = TplDataChannel.objects.filter(devtemplate=devtemplates_pk)
        serializer = TplDataChannelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, devtemplates_pk=None):
        queryset = TplDataChannel.objects.filter(pk=pk, devtemplate=devtemplates_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = TplDataChannelSerializer(queryset_tmp)
        return Response(serializer.data)


class TplDataUnitViewSet(viewsets.ModelViewSet):
    """
    list:
    查询数值单位列表

    create:
    创建数值单位

    retrieve:
    查询数值单位详情

    update:
    更新数值单位

    partial_update:
    更新数值单位部分属性

    destroy:
    删除数值单位

    """

    serializer_class = TplDataUnitSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = TplDataUnit.objects.all()
           
    def list(self, request, devtemplates_pk=None,tpldatachannels_pk=None):
        queryset = TplDataUnit.objects.filter(tpldatachannel=tpldatachannels_pk)
        serializer = TplDataUnitSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, devtemplates_pk=None,tpldatachannels_pk=None):
        queryset = TplDataUnit.objects.filter(pk=pk,tpldatachannel=tpldatachannels_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = TplDataUnitSerializer(queryset_tmp)
        return Response(serializer.data)


class TplCtrlChannelViewSet(viewsets.ModelViewSet):
    """
    list:
    查询模板控制通道列表

    create:
    创建模板控制通道

    retrieve:
    查询模板控制通道详情

    update:
    更新模板控制通道

    partial_update:
    更新模板控制通道部分属性

    destroy:
    删除模板控制通道

    """

    serializer_class = TplCtrlChannelSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = TplCtrlChannel.objects.all()
           
    def list(self, request, devtemplates_pk=None):
        queryset = TplCtrlChannel.objects.filter(devtemplate=devtemplates_pk)
        serializer = TplCtrlChannelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, devtemplates_pk=None):
        queryset = TplCtrlChannel.objects.filter(pk=pk, devtemplate=devtemplates_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = TplCtrlChannelSerializer(queryset_tmp)
        return Response(serializer.data)


class TplCtrlUnitViewSet(viewsets.ModelViewSet):
    """
    list:
    查询数值单位列表

    create:
    创建数值单位

    retrieve:
    查询数值单位详情

    update:
    更新数值单位

    partial_update:
    更新数值单位部分属性

    destroy:
    删除数值单位

    """

    serializer_class = TplCtrlUnitSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = TplCtrlUnit.objects.all()
           
    def list(self, request, devtemplates_pk=None,tplctrlchannels_pk=None):
        queryset = TplCtrlUnit.objects.filter(tplctrlchannel=tplctrlchannels_pk)
        serializer = TplCtrlUnitSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, devtemplates_pk=None,tplctrlchannels_pk=None):
        queryset = TplCtrlUnit.objects.filter(pk=pk,tplctrlchannel=tplctrlchannels_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = TplCtrlUnitSerializer(queryset_tmp)
        return Response(serializer.data)