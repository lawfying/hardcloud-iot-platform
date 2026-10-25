from django.shortcuts import render
from .models import Device,DeviceTags,DataChannel,DataUnit,CtrlChannel,CtrlUnit,MetricData,TextData,SwitchData,GPSData,\
Measurement,Message,SwitchStatus,Position,IntervalScheduleDev,CrontabScheduleDev,ClockedScheduleDev,PeriodicTaskDev,\
    DeviceHttpAction,DeviceMqttAction,DeviceTriggerjobHttp,DeviceTriggerjobMqtt
from .serializers import DeviceSerializer,DeviceTagsSerializer,DataChannelSerializer,DataUnitSerializer,CtrlChannelSerializer,\
CtrlUnitSerializer,MetricDataSerializer,TextDataSerializer,SwitchDataSerializer,GPSDataSerializer,MeasurementSerializer,\
MessageSerializer,SwitchStatusSerializer,PositionSerializer,\
    IntervalScheduleDevSerializer,CrontabScheduleDevSerializer,ClockedScheduleDevSerializer,PeriodicTaskDevSerializer,\
        DeviceHttpActionSerializer,DeviceMqttActionSerializer,DeviceTriggerjobHttpSerializer,DeviceTriggerjobMqttSerializer
    
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
from rest_framework import status

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from datetime import datetime,timedelta
from django.conf import settings

from devtemplate.models import DevTemplate,TemplateTags,TplDataChannel,TplDataUnit,TplCtrlChannel,TplCtrlUnit

from trigger.tasks import createByTemplatetask
import json
import paho.mqtt.publish as publish

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class DeviceViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备列表

    create:
    创建设备

    retrieve:
    查询设备详情

    update:
    更新设备

    partial_update:
    更新设备部分属性

    destroy:
    删除设备

    createDevByTpl:
    根据提供的模板创建设备及相关的数据、控制通道

    """

    serializer_class = DeviceSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = Device.objects.all()

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)

    def list(self, request,):

        queryset = Device.objects.filter(owner=request.user).order_by('-created')

        self.check_object_permissions(request,Device)
        serializer = DeviceSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Device.objects.filter(owner=request.user)
        queryset_tmp = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(request,Device)
        serializer = DeviceSerializer(queryset_tmp)
        return Response(serializer.data)

 
    @list_route(methods=['post'])
    def createDevByTpl(self, request,):

        try:
            if request.method == 'POST':
                devtpl = request.data['devtemplate']
                tpl = DevTemplate.objects.get(id=devtpl)
                dev = Device(title=tpl.title,description=tpl.description,img=tpl.img,device_type=tpl.device_type,\
                    is_custom_registered=tpl.is_custom_registered,protocal_type=tpl.protocal_type,owner=tpl.owner)
                dev.save()
                serializer = DeviceSerializer(dev)
                try:
                    createByTemplatetask.delay(str(dev.id),devtpl)
                except:
                    pass
                # #tags 
                # tpltags = TemplateTags.objects.filter(devtemplate=devtpl)
                # for tmptag in tpltags:
                #     devtag = DeviceTags(device=dev,key=tmptag.key,value=tmptag.value)
                #     devtag.save()
                # #the following is copy control channel
                # tplcch = TplCtrlChannel.objects.filter(devtemplate=devtpl)
                # for tmptplcch in tplcch:
                #     ctrlch = CtrlChannel(device=dev,title=tmptplcch.title, datatype=tmptplcch.datatype)
                #     ctrlch.save()
                #     if (ctrlch.datatype == 'DECIMAL'):
                #         tplunit = TplCtrlUnit.objects.get(tplctrlchannel=tmptplcch)
                #         ctrlunit = CtrlUnit(ctrlchannel=ctrlch,unitlabel=tplunit.unitlabel,symbol=tplunit.symbol,max_value=tplunit.max_value,min_value=tplunit.min_value,step=tplunit.step)
                #         ctrlunit.save()
                # #data channel
                # tpldch = TplDataChannel.objects.filter(devtemplate=devtpl)
                # print(tpldch)
                # for tmptpldch in tpldch:
                #     # copy data channel
                #     datach = DataChannel(device=dev,title= tmptpldch.title, datatype=tmptpldch.datatype)
                #     datach.save()
                #     # if datatype is decimal,copy the data unit.
                #     if datach.datatype == 'DECIMAL':
                #         tplunit = TplDataUnit.objects.get(tpldatachannel=tmptpldch)
                #         dataunit = DataUnit(datachannel=datach,unitlabel=tplunit.unitlabel,symbol=tplunit.symbol,max_value=tplunit.max_value,min_value=tplunit.min_value,step=tplunit.step)
                #         dataunit.save()
                #         print("test")
                return Response(serializer.data)

            else:
                return JSONResponse(["no content"])
        except:
                #return Response(serializer.data)
                return JSONResponse(["exception"])

class DeviceTagsViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备标签列表

    create:
    创建设备标签

    retrieve:
    查询设备标签详情

    update:
    更新设备标签

    partial_update:
    更新设备标签部分属性

    destroy:
    删除设备标签

    """	

    serializer_class = DeviceTagsSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = DeviceTags.objects.all()
           
    def list(self, request, devices_pk=None):
        queryset = DeviceTags.objects.filter(device=devices_pk)
        serializer = DeviceTagsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None,devices_pk=None):
        queryset = DeviceTags.objects.filter(pk=pk, device=devices_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = DeviceTagsSerializer(queryset_tmp)
        return Response(serializer.data)



class DataChannelViewSet(viewsets.ModelViewSet):
    """
    list:
    查询数据通道列表

    create:
    创建数据通道

    retrieve:
    查询数据通道详情

    update:
    更新数据通道

    partial_update:
    更新数据通道部分属性

    destroy:
    删除数据通道

    """
    serializer_class = DataChannelSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = DataChannel.objects.all()
           
    def list(self, request, devices_pk=None):
        queryset = DataChannel.objects.filter(device=devices_pk)
        serializer = DataChannelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, devices_pk=None):
        queryset = DataChannel.objects.filter(pk=pk, device=devices_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = DataChannelSerializer(queryset_tmp)
        return Response(serializer.data)


class DataUnitViewSet(viewsets.ModelViewSet):
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

    serializer_class = DataUnitSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = DataUnit.objects.all()
           
    def list(self, request, devices_pk=None,datachannels_pk=None):
        queryset = DataUnit.objects.filter(datachannel=datachannels_pk)
        serializer = DataUnitSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, devices_pk=None,datachannels_pk=None):
        queryset = DataUnit.objects.filter(pk=pk,datachannel=datachannels_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = DataUnitSerializer(queryset_tmp)
        return Response(serializer.data)


class CtrlChannelViewSet(viewsets.ModelViewSet):
    """
    list:
    查询控制通道列表

    create:
    创建控制通道

    retrieve:
    查询控制通道详情

    update:
    更新控制通道

    partial_update:
    更新控制通道部分属性

    destroy:
    删除控制通道

    """

    serializer_class = CtrlChannelSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = CtrlChannel.objects.all()
           
    def list(self, request, devices_pk=None):
        queryset = CtrlChannel.objects.filter(device=devices_pk)
        # serializer = CtrlChannelSerializer(queryset, many=True)
        # return Response(serializer.data)
        tmplist = []
        for dl in queryset:
            tmplist.append({"id":dl.id,"device":dl.device.id,"title":dl.title,"datatype":dl.datatype,"device_title":dl.device.title})
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None, devices_pk=None):
        queryset = CtrlChannel.objects.filter(pk=pk, device=devices_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = CtrlChannelSerializer(queryset_tmp)
        return Response(serializer.data)


class CtrlUnitViewSet(viewsets.ModelViewSet):
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

    serializer_class = CtrlUnitSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = CtrlUnit.objects.all()
           
    def list(self, request, devices_pk=None,ctrlchannels_pk=None):
        queryset = CtrlUnit.objects.filter(ctrlchannel=ctrlchannels_pk)
        serializer = CtrlUnitSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, devices_pk=None,ctrlchannels_pk=None):
        queryset = CtrlUnit.objects.filter(pk=pk,ctrlchannel=ctrlchannels_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = CtrlUnitSerializer(queryset_tmp)
        return Response(serializer.data)

class MetricDataViewSet(viewsets.ModelViewSet):
    """
    list:
    查询数据点列表

    create:
    提交数值数据
    如果方向为DOWN，支持MQTT发布消息

    retrieve:
    查询数值数据详情

    update:
    更新数值数据，不建议使用

    partial_update:
    更新数值数据部分属性，不建议使用

    destroy:
    删除数值单位

    latestvalue:
    查询最新的数据
    数据方向，UP：表示查询最新上传的数据；DOWN:表示查询设备最新接收的数据;POST:direction = UP or DOWN.

    range:
    查询某一时间段的数据
    数据方向，UP:表示查询的是设备上传的数据，DOWN:表示查询的是设备接收的数据；时间字符串：2019-04-04 00:29:00；时间格式：%Y-%m-%d %H:%M:%S;POST:from_date = 2019-04-04 00:29:00
         to_date = 2019-04-05 00:29:00;date_format = %Y-%m-%d %H:%M:%S;direction = UP or DOWN.
    """

    serializer_class = MetricDataSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = MetricData.objects.all()
      
    def list(self, request, devices_pk=None,ctrlchannels_pk=None):
        queryset = MetricData.objects.filter(ctrlchannel=ctrlchannels_pk)
        serializer = MetricDataSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self,request,devices_pk=None,ctrlchannels_pk=None):
        serializer = MetricDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #以下支持MQTT发布
            try:
                if request.data["direction"] == "DOWN":
                    payload = json.dumps(request.data)
                    #publish.single(ctrlchannels_pk, payload,hostname=settings.MQTT_HOST,auth={'username':settings.MQTT_USERNAME, 'password':settings.MQTT_PASSWORD})
                    publish.single(ctrlchannels_pk, payload,hostname=settings.MQTT_HOST)
            except:
                pass
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

    def retrieve(self, request, pk=None, devices_pk=None,ctrlchannels_pk=None):
        queryset = MetricData.objects.filter(pk=pk,ctrlchannel=ctrlchannels_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = MetricDataSerializer(queryset_tmp)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def latestoneday(self, request, devices_pk=None,ctrlchannels_pk=None):

        try:
            if request.method == 'GET':
                end_date = datetime.now()
                start_date = end_date - timedelta(days=1)
                queryset = MetricData.objects.filter(timestamp__gte=start_date,timestamp__lte=end_date,ctrlchannel=ctrlchannels_pk)
                serializer = MetricDataSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['post'])
    def latestvalue(self, request, devices_pk=None,ctrlchannels_pk=None):

        try:
            if request.method == 'POST':
                req_direction = request.data['direction']
                queryset = MetricData.objects.filter(ctrlchannel=ctrlchannels_pk,direction=req_direction)
                serializer = MetricDataSerializer(queryset, many=True)
                return Response(serializer.data[-1])
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['post'])
    def range(self, request, devices_pk=None,ctrlchannels_pk=None):
        #数据的查询
        #UP:表示查询的是设备上传的数据，DOWN:表示查询的是设备接收的数据
        #时间字符串：2019-04-04 00:29:00
        #时间格式：%Y-%m-%d %H:%M:%S
        try:
            if request.method == 'POST':
                req_from_date = request.data['from_date']
                req_to_date  = request.data['to_date']
                req_date_format = request.data['date_format']
                req_direction = request.data['direction']
                #strptime 把时间转换为时间戳
                start_date = datetime.strptime(req_from_date,req_date_format)
                end_date = datetime.strptime(req_to_date,req_date_format)
                queryset = MetricData.objects.filter(timestamp__range=(start_date,end_date),ctrlchannel=ctrlchannels_pk,direction=req_direction)
                serializer = MetricDataSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

class TextDataViewSet(viewsets.ModelViewSet):
    """
    list:
    查询文本列表

    create:
    提交文本数据
    如果方向为DOWN，支持MQTT发布消息

    retrieve:
    查询文本详情

    update:
    更新文本数据，不建议使用

    partial_update:
    更新文本数据部分属性，不建议使用

    destroy:
    删除文本数据

    latestvalue:
    查询最新的文本数据
    数据方向，UP：表示查询最新上传的数据；DOWN:表示查询设备最新接收的数据;POST:direction = UP or DOWN.

    range:
    查询某一时间段的文本数据
    数据方向，UP:表示查询的是设备上传的数据，DOWN:表示查询的是设备接收的数据；时间字符串：2019-04-04 00:29:00；时间格式：%Y-%m-%d %H:%M:%S;POST:from_date = 2019-04-04 00:29:00
         to_date = 2019-04-05 00:29:00;date_format = %Y-%m-%d %H:%M:%S;direction = UP or DOWN.
    """

    serializer_class = TextDataSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = TextData.objects.all()
      

    def list(self, request, devices_pk=None,ctrlchannels_pk=None):
        queryset = TextData.objects.filter(ctrlchannel=ctrlchannels_pk)
        serializer = TextDataSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self,request,devices_pk=None,ctrlchannels_pk=None):
        serializer = TextDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #以下支持MQTT发布
            try:
                if request.data["direction"] == "DOWN":
                    print('test')
                    payload = json.dumps(request.data)
                    print(payload)
                    #publish.single(ctrlchannels_pk, payload,hostname=settings.MQTT_HOST,auth={'username':settings.MQTT_USERNAME, 'password':settings.MQTT_PASSWORD})
                    publish.single(ctrlchannels_pk, payload,hostname=settings.MQTT_HOST)
            except:
                pass
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, devices_pk=None,ctrlchannels_pk=None):
        queryset = TextData.objects.filter(pk=pk,ctrlchannel=ctrlchannels_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = TextDataSerializer(queryset_tmp)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def latestoneday(self, request, devices_pk=None,ctrlchannels_pk=None):

        try:
            if request.method == 'GET':
                end_date = datetime.now()
                start_date = end_date - timedelta(days=1)
                queryset = TextData.objects.filter(timestamp__gte=start_date,timestamp__lte=end_date,ctrlchannel=ctrlchannels_pk)
                serializer = TextDataSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['post'])
    def latestvalue(self, request, devices_pk=None,ctrlchannels_pk=None):

        try:
            if request.method == 'POST':
                req_direction = request.data['direction']
                queryset = TextData.objects.filter(ctrlchannel=ctrlchannels_pk,direction=req_direction)
                serializer = TextDataSerializer(queryset, many=True)
                return Response(serializer.data[-1])
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['post'])
    def range(self, request, devices_pk=None,ctrlchannels_pk=None):
        #数据的查询
        #UP:表示查询的是设备上传的数据，DOWN:表示查询的是设备接收的数据
        #时间字符串：2019-04-04 00:29:00
        #时间格式：%Y-%m-%d %H:%M:%S
        try:
            if request.method == 'POST':
                req_from_date = request.data['from_date']
                req_to_date  = request.data['to_date']
                req_date_format = request.data['date_format']
                req_direction = request.data['direction']
                #strptime 把时间转换为时间戳
                start_date = datetime.strptime(req_from_date,req_date_format)
                end_date = datetime.strptime(req_to_date,req_date_format)
                queryset = TextcData.objects.filter(timestamp__range=(start_date,end_date),ctrlchannel=ctrlchannels_pk,direction=req_direction)
                serializer = TextDataSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

class SwitchDataViewSet(viewsets.ModelViewSet):
    """
    list:
    查询开关数据列表

    create:
    提交开关数据
    如果方向为DOWN，支持MQTT发布消息

    retrieve:
    查询开关数据详情

    update:
    更新开关数据，不建议使用

    partial_update:
    更新开关数据部分属性，不建议使用

    destroy:
    删除开关数据

    latestvalue:
    查询最新的开关数据
    数据方向，UP：表示查询最新上传的数据；DOWN:表示查询设备最新接收的数据;POST:direction = UP or DOWN.

    range:
    查询某一时间段的开关数据
    数据方向，UP:表示查询的是设备上传的数据，DOWN:表示查询的是设备接收的数据；时间字符串：2019-04-04 00:29:00；时间格式：%Y-%m-%d %H:%M:%S;POST:from_date = 2019-04-04 00:29:00
         to_date = 2019-04-05 00:29:00;date_format = %Y-%m-%d %H:%M:%S;direction = UP or DOWN.
    """

    serializer_class = SwitchDataSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = SwitchData.objects.all()

    def list(self, request, devices_pk=None,ctrlchannels_pk=None):
        queryset = SwitchData.objects.filter(ctrlchannel=ctrlchannels_pk)
        serializer = SwitchDataSerializer(queryset, many=True)
        return Response(serializer.data)
  
    def create(self,request,devices_pk=None,ctrlchannels_pk=None):
        serializer = SwitchDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #以下支持MQTT发布
            try:
                if request.data["direction"] == "DOWN":
                    payload = json.dumps(request.data)
                    #publish.single(ctrlchannels_pk, payload,hostname=settings.MQTT_HOST,auth={'username':settings.MQTT_USERNAME, 'password':settings.MQTT_PASSWORD})
                    publish.single(ctrlchannels_pk, payload,hostname=settings.MQTT_HOST)
            except:
                pass
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, devices_pk=None,ctrlchannels_pk=None):
        queryset = SwitchData.objects.filter(pk=pk,ctrlchannel=ctrlchannels_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = SwitchDataSerializer(queryset_tmp)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def latestoneday(self, request, devices_pk=None,ctrlchannels_pk=None):

        try:
            if request.method == 'GET':
                end_date = datetime.now()
                start_date = end_date - timedelta(days=1)
                queryset = SwitchData.objects.filter(timestamp__gte=start_date,timestamp__lte=end_date,ctrlchannel=ctrlchannels_pk)
                serializer = SwitchDataSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['post'])
    def latestvalue(self, request, devices_pk=None,ctrlchannels_pk=None):

        try:
            if request.method == 'POST':
                req_direction = request.data['direction']
                queryset = SwitchData.objects.filter(ctrlchannel=ctrlchannels_pk,direction=req_direction)
                serializer = SwitchDataSerializer(queryset, many=True)
                return Response(serializer.data[-1])
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['post'])
    def range(self, request, devices_pk=None,ctrlchannels_pk=None):
        #数据的查询
        #UP:表示查询的是设备上传的数据，DOWN:表示查询的是设备接收的数据
        #时间字符串：2019-04-04 00:29:00
        #时间格式：%Y-%m-%d %H:%M:%S
        try:
            if request.method == 'POST':
                req_from_date = request.data['from_date']
                req_to_date  = request.data['to_date']
                req_date_format = request.data['date_format']
                req_direction = request.data['direction']
                #strptime 把时间转换为时间戳
                start_date = datetime.strptime(req_from_date,req_date_format)
                end_date = datetime.strptime(req_to_date,req_date_format)
                queryset = SwitchData.objects.filter(timestamp__range=(start_date,end_date),ctrlchannel=ctrlchannels_pk,direction=req_direction)
                serializer = SwitchDataSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

class GPSDataViewSet(viewsets.ModelViewSet):
    """
    list:
    查询GPS数据列表

    create:
    提交GPS数据
    如果方向为DOWN，支持MQTT发布消息

    retrieve:
    查询GPS数据详情

    update:
    更新GPS数据，不建议使用

    partial_update:
    更新GPS数据部分属性，不建议使用

    destroy:
    删除GPS数据

    latestvalue:
    查询最新的GPS数据
    数据方向，UP：表示查询最新上传的数据；DOWN:表示查询设备最新接收的数据;POST:direction = UP or DOWN.

    range:
    查询某一时间段的GPS数据
    数据方向，UP:表示查询的是设备上传的数据，DOWN:表示查询的是设备接收的数据；时间字符串：2019-04-04 00:29:00；时间格式：%Y-%m-%d %H:%M:%S;POST:from_date = 2019-04-04 00:29:00
         to_date = 2019-04-05 00:29:00;date_format = %Y-%m-%d %H:%M:%S;direction = UP or DOWN.
    """

    serializer_class = GPSDataSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = GPSData.objects.all()
      

    def list(self, request, devices_pk=None,ctrlchannels_pk=None):
        queryset = GPSData.objects.filter(ctrlchannel=ctrlchannels_pk)
        serializer = GPSDataSerializer(queryset, many=True)
        return Response(serializer.data)
   
    def create(self,request,devices_pk=None,ctrlchannels_pk=None):
        serializer = GPSDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #以下支持MQTT发布
            try:
                if request.data["direction"] == "DOWN":
                    payload = json.dumps(request.data)
                    #publish.single(ctrlchannels_pk, payload,hostname=settings.MQTT_HOST,auth={'username':settings.MQTT_USERNAME, 'password':settings.MQTT_PASSWORD})
                    publish.single(ctrlchannels_pk, payload,hostname=settings.MQTT_HOST)
            except:
                pass
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, devices_pk=None,ctrlchannels_pk=None):
        queryset = GPSData.objects.filter(pk=pk,ctrlchannel=ctrlchannels_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = GPSDataSerializer(queryset_tmp)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def latestoneday(self, request, devices_pk=None,ctrlchannels_pk=None):

        try:
            if request.method == 'GET':
                end_date = datetime.now()
                start_date = end_date - timedelta(days=1)
                queryset = GPSData.objects.filter(timestamp__gte=start_date,timestamp__lte=end_date,ctrlchannel=ctrlchannels_pk)
                serializer = GPSDataSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['post'])
    def latestvalue(self, request, devices_pk=None,ctrlchannels_pk=None):

        try:
            if request.method == 'POST':
                req_direction = request.data['direction']
                queryset = GPSData.objects.filter(ctrlchannel=ctrlchannels_pk,direction=req_direction)
                serializer = GPSDataSerializer(queryset, many=True)
                return Response(serializer.data[-1])
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['post'])
    def range(self, request, devices_pk=None,ctrlchannels_pk=None):
        #数据的查询
        #UP:表示查询的是设备上传的数据，DOWN:表示查询的是设备接收的数据
        #时间字符串：2019-04-04 00:29:00
        #时间格式：%Y-%m-%d %H:%M:%S
        try:
            if request.method == 'POST':
                req_from_date = request.data['from_date']
                req_to_date  = request.data['to_date']
                req_date_format = request.data['date_format']
                req_direction = request.data['direction']
                #strptime 把时间转换为时间戳
                start_date = datetime.strptime(req_from_date,req_date_format)
                end_date = datetime.strptime(req_to_date,req_date_format)
                queryset = GPSData.objects.filter(timestamp__range=(start_date,end_date),ctrlchannel=ctrlchannels_pk,direction=req_direction)
                serializer = GPSDataSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])


#以下操作的是mongodb
class MeasurementViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备上传数据列表

    create:
    提交设备上传数据

    retrieve:
    查询设备上传数据详情
    id为mongodb的文档_id

    update:
    更新设备上传数据，不建议使用
    id为mongodb的文档_id

    partial_update:
    更新设备上传数据部分属性，不建议使用
    id为mongodb的文档_id

    destroy:
    删除设备上传数据
    id为mongodb的文档_id

    latestvalue:
    查询最新的设备上传数据

    range:
    查询某一时间段的设备上传数据
    时间字符串：2019-04-04 00:29:00；时间格式：%Y-%m-%d %H:%M:%S;POST:from_date = 2019-04-04 00:29:00
         to_date = 2019-04-05 00:29:00;date_format = %Y-%m-%d %H:%M:%S。
    
    """

    serializer_class = MeasurementSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = Measurement.objects.all()
      

    def list(self, request, devices_pk=None,datachannels_pk=None):
        queryset = Measurement.objects(datachannel=datachannels_pk)
        serializer = MeasurementSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request,devices_pk=None,datachannels_pk=None):
        try:
            if request.method == 'POST':
                value = float(request.data['value'])
                timestamp = datetime.now()
                measurement_obj = Measurement(datachannel=datachannels_pk,timestamp=timestamp,value=value)
                measurement_obj.save()
                info = {'datachannel':datachannels_pk,'timestamp':timestamp,'value':value}
                return JSONResponse(info)  

            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])
             

    @list_route(methods=['get'])
    def latestvalue(self, request, devices_pk=None,datachannels_pk=None):

        try:
            if request.method == 'GET':
                queryset = Measurement.objects(datachannel=datachannels_pk)
                serializer = MeasurementSerializer(queryset, many=True)
                return Response(serializer.data[-1])
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['get'])
    def latestoneday(self, request, devices_pk=None,datachannels_pk=None):

        try:
            if request.method == 'GET':
                end_date = datetime.now()
                start_date = end_date - timedelta(days=1)
                queryset = Measurement.objects(timestamp__gte=start_date,timestamp__lte=end_date,datachannel=datachannels_pk)
                serializer = MeasurementSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])


    @list_route(methods=['post'])
    def range(self, request, devices_pk=None,datachannels_pk=None):
        #数据的查询
        #时间字符串：2019-04-04 00:29:00
        #时间格式：%Y-%m-%d %H:%M:%S
        try:
            if request.method == 'POST':
                req_from_date = request.data['from_date']
                req_to_date  = request.data['to_date']
                req_date_format = request.data['date_format']
                #strptime 把时间转换为时间戳
                start_date = datetime.strptime(req_from_date,req_date_format)
                end_date = datetime.strptime(req_to_date,req_date_format)
                queryset = Measurement.objects(timestamp__gte=start_date,timestamp__lte=end_date,datachannel=datachannels_pk)
                serializer = MeasurementSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])


#以下操作的是mongodb
class MessageViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备上传文本列表

    create:
    提交设备上传文本

    retrieve:
    查询设备上传文本详情
    id为mongodb的文档_id

    update:
    更新设备上传文本数据,不建议使用
    id为mongodb的文档_id

    partial_update:
    更新设备上传文本数据部分属性，不建议使用
    id为mongodb的文档_id

    destroy:
    删除设备上传文本数据
    id为mongodb的文档_id

    latestvalue:
    查询最新的设备上传文本数据

    range:
    查询某一时间段的设备上传数据
    时间字符串：2019-04-04 00:29:00；时间格式：%Y-%m-%d %H:%M:%S;POST:from_date = 2019-04-04 00:29:00
         to_date = 2019-04-05 00:29:00;date_format = %Y-%m-%d %H:%M:%S。
    
    """

    serializer_class = MessageSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = Message.objects.all()
      

    def list(self, request, devices_pk=None,datachannels_pk=None):
        queryset = Message.objects(datachannel=datachannels_pk)
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request,devices_pk=None,datachannels_pk=None):
        try:
            if request.method == 'POST':
                message = request.data['message']
                timestamp = datetime.now()
                message_obj = Message(datachannel=datachannels_pk,timestamp=timestamp,message=message)
                message_obj.save()
                info = {'datachannel':datachannels_pk,'timestamp':timestamp,'message':message}
                return JSONResponse(info)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['get'])
    def latestoneday(self, request, devices_pk=None,datachannels_pk=None):

        try:
            if request.method == 'GET':
                end_date = datetime.now()
                start_date = end_date - timedelta(days=1)
                queryset = Message.objects(timestamp__gte=start_date,timestamp__lte=end_date,datachannel=datachannels_pk)
                serializer = MessageSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['get'])
    def latestvalue(self, request, devices_pk=None,datachannels_pk=None):

        try:
            if request.method == 'GET':
                queryset = Message.objects(datachannel=datachannels_pk)
                serializer = MessageSerializer(queryset, many=True)
                return Response(serializer.data[-1])
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])


    @list_route(methods=['post'])
    def range(self, request, devices_pk=None,datachannels_pk=None):
        #数据的查询
        #时间字符串：2019-04-04 00:29:00
        #时间格式：%Y-%m-%d %H:%M:%S
        try:
            if request.method == 'POST':
                req_from_date = request.data['from_date']
                req_to_date  = request.data['to_date']
                req_date_format = request.data['date_format']
                #strptime 把时间转换为时间戳
                start_date = datetime.strptime(req_from_date,req_date_format)
                end_date = datetime.strptime(req_to_date,req_date_format)
                queryset = Message.objects(timestamp__gte=start_date,timestamp__lte=end_date,datachannel=datachannels_pk)
                serializer = MessageSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

#以下操作的是mongodb
class SwitchStatusViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备上传开关状态列表

    create:
    提交设备上传开关状态

    retrieve:
    查询设备上传开关状态详情
    id为mongodb的文档_id

    update:
    更新设备上传开关状态数据,不建议使用
    id为mongodb的文档_id

    partial_update:
    更新设备上传文本开关状态部分属性，不建议使用
    id为mongodb的文档_id

    destroy:
    删除设备上传开关状态数据
    id为mongodb的文档_id

    latestvalue:
    查询最新的设备上传开关状态数据

    range:
    查询某一时间段的设备上传数据
    时间字符串：2019-04-04 00:29:00；时间格式：%Y-%m-%d %H:%M:%S;POST:from_date = 2019-04-04 00:29:00
         to_date = 2019-04-05 00:29:00;date_format = %Y-%m-%d %H:%M:%S。
    
    """

    serializer_class = SwitchStatusSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = SwitchStatus.objects.all()
      

    def list(self, request, devices_pk=None,datachannels_pk=None):
        queryset = SwitchStatus.objects(datachannel=datachannels_pk)
        serializer = SwitchStatusSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request,devices_pk=None,datachannels_pk=None):
        try:
            if request.method == 'POST':
                status = bool(int(request.data['status']))
                timestamp = datetime.now()
                obj_tmp = SwitchStatus(datachannel=datachannels_pk,timestamp=timestamp,status=status)
                obj_tmp.save()
                info = {'datachannel':datachannels_pk,'timestamp':timestamp,'status':status}
                return JSONResponse(info)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['get'])
    def latestoneday(self, request, devices_pk=None,datachannels_pk=None):

        try:
            if request.method == 'GET':
                end_date = datetime.now()
                start_date = end_date - timedelta(days=1)
                queryset = SwitchStatus.objects(timestamp__gte=start_date,timestamp__lte=end_date,datachannel=datachannels_pk)
                serializer = SwitchStatusSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['get'])
    def latestvalue(self, request, devices_pk=None,datachannels_pk=None):

        try:
            if request.method == 'GET':
                queryset = SwitchStatus.objects(datachannel=datachannels_pk)
                serializer = SwitchStatusSerializer(queryset, many=True)
                return Response(serializer.data[-1])
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])


    @list_route(methods=['post'])
    def range(self, request, devices_pk=None,datachannels_pk=None):
        #数据的查询
        #时间字符串：2019-04-04 00:29:00
        #时间格式：%Y-%m-%d %H:%M:%S
        try:
            if request.method == 'POST':
                req_from_date = request.data['from_date']
                req_to_date  = request.data['to_date']
                req_date_format = request.data['date_format']
                #strptime 把时间转换为时间戳
                start_date = datetime.strptime(req_from_date,req_date_format)
                end_date = datetime.strptime(req_to_date,req_date_format)
                queryset = SwitchStatus.objects(timestamp__gte=start_date,timestamp__lte=end_date,datachannel=datachannels_pk)
                serializer = SwitchStatusSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

#以下操作的是mongodb
class PositionViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备上传位置数据列表

    create:
    提交设备上传位置数据

    retrieve:
    查询设备上传位置数据详情
    id为mongodb的文档_id

    update:
    更新设备上传位置数据,不建议使用
    id为mongodb的文档_id

    partial_update:
    更新设备上传位置数据部分属性，不建议使用
    id为mongodb的文档_id

    destroy:
    删除设备上传位置数据
    id为mongodb的文档_id

    latestvalue:
    查询最新的设备上传位置数据

    range:
    查询某一时间段的设备上传数据
    时间字符串：2019-04-04 00:29:00；时间格式：%Y-%m-%d %H:%M:%S;POST:from_date = 2019-04-04 00:29:00
         to_date = 2019-04-05 00:29:00;date_format = %Y-%m-%d %H:%M:%S。
    
    """

    serializer_class = PositionSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = Position.objects.all()
      

    def list(self, request, devices_pk=None,datachannels_pk=None):
        queryset = Position.objects(datachannel=datachannels_pk)
        serializer = PositionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request,devices_pk=None,datachannels_pk=None):
        try:
            if request.method == 'POST':
                latitude = float(request.data['latitude'])
                longitude = float(request.data['longitude'])
                elevation = float(request.data['elevation'])
                address = request.data['address']
                timestamp = datetime.now()
                obj_tmp = Position(datachannel=datachannels_pk,timestamp=timestamp,latitude=latitude,longitude=longitude,elevation=elevation,address=address)
                obj_tmp.save()
                info = {'datachannel':datachannels_pk,'timestamp':timestamp,'latitude':latitude,'longitude':longitude,'elevation':elevation,'address':address}
                return JSONResponse(info)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['get'])
    def latestoneday(self, request, devices_pk=None,datachannels_pk=None):

        try:
            if request.method == 'GET':
                end_date = datetime.now()
                start_date = end_date - timedelta(days=1)
                queryset = Position.objects(timestamp__gte=start_date,timestamp__lte=end_date,datachannel=datachannels_pk)
                serializer = PositionSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

    @list_route(methods=['get'])
    def latestvalue(self, request, devices_pk=None,datachannels_pk=None):

        try:
            if request.method == 'GET':
                queryset = Position.objects(datachannel=datachannels_pk)
                serializer = PositionSerializer(queryset, many=True)
                return Response(serializer.data[-1])
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])


    @list_route(methods=['post'])
    def range(self, request, devices_pk=None,datachannels_pk=None):
        #数据的查询
        #时间字符串：2019-04-04 00:29:00
        #时间格式：%Y-%m-%d %H:%M:%S
        try:
            if request.method == 'POST':
                req_from_date = request.data['from_date']
                req_to_date  = request.data['to_date']
                req_date_format = request.data['date_format']
                #strptime 把时间转换为时间戳
                start_date = datetime.strptime(req_from_date,req_date_format)
                end_date = datetime.strptime(req_to_date,req_date_format)
                queryset = Position.objects(timestamp__gte=start_date,timestamp__lte=end_date,datachannel=datachannels_pk)
                serializer = PositionSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JSONResponse(["no content"])
        except:
                return JSONResponse(["exception"])

class IntervalScheduleDevViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备相关的间隔时间计划列表

    create:
    创建设备相关的间隔时间计划

    retrieve:
    查询设备相关的间隔时间计划详情

    update:
    更新设备相关的间隔时间计划

    partial_update:
    更新设备相关的间隔时间计划部分属性

    destroy:
    删除设备相关的间隔时间计划

    """	

    serializer_class = IntervalScheduleDevSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset =IntervalScheduleDev.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
           
    def list(self, request, devices_pk=None):
        queryset = IntervalScheduleDev.objects.filter(device=devices_pk)
        # serializer = IntervalScheduleDevSerializer(queryset, many=True)
        # return Response(serializer.data)
        tmplist = []
        for dl in queryset: #('id','every','period','owner','device')
            tmplist.append({'id':dl.id,'every':dl.every,'period':dl.period,'owner':dl.owner.id,'device_id':dl.device.id,'device_title':dl.device.title})
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None,devices_pk=None):
        queryset = IntervalScheduleDev.objects.filter(pk=pk, device=devices_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = IntervalScheduleDevSerializer(queryset_tmp)
        return Response(serializer.data)

class CrontabScheduleDevViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备相关的例行时间计划列表

    create:
    创建设备相关的例行时间计划

    retrieve:
    查询设备相关的例行时间计划详情

    update:
    更新设备相关的例行时间计划

    partial_update:
    更新设备相关的例行时间计划部分属性

    destroy:
    删除设备相关的例行时间计划

    """	

    serializer_class = CrontabScheduleDevSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset =CrontabScheduleDev.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
           
    def list(self, request, devices_pk=None):
        queryset = CrontabScheduleDev.objects.filter(device=devices_pk)
        # serializer = CrontabScheduleDevSerializer(queryset, many=True)
        # return Response(serializer.data)
        tmplist = []
        for dl in queryset: #('id','minute','hour','day_of_week','day_of_month','month_of_year','owner','device')
            tmplist.append({'id':dl.id,'minute':dl.minute,'hour':dl.hour,'day_of_week':dl.day_of_week,'day_of_month':dl.day_of_month,'month_of_year':dl.month_of_year,'owner':dl.owner.id,'device_id':dl.device.id,'device_title':dl.device.title})
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None,devices_pk=None):
        queryset = CrontabScheduleDev.objects.filter(pk=pk, device=devices_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = CrontabScheduleDevSerializer(queryset_tmp)
        return Response(serializer.data)


class ClockedScheduleDevViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备相关的定时时间计划列表

    create:
    创建设备相关的定时时间计划

    retrieve:
    查询设备相关的定时时间计划详情

    update:
    更新设备相关的定时时间计划

    partial_update:
    更新设备相关的定时时间计划部分属性

    destroy:
    删除设备相关的定时时间计划

    """	

    serializer_class = ClockedScheduleDevSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset =ClockedScheduleDev.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
           
    def list(self, request, devices_pk=None):
        queryset = ClockedScheduleDev.objects.filter(device=devices_pk)
        # serializer = ClockedScheduleDevSerializer(queryset, many=True)
        # return Response(serializer.data)
        tmplist = []
        for dl in queryset: #('id','clocked_time','enabled','owner','device')
            tmplist.append({'id':dl.id,'clocked_time':dl.clocked_time,'enabled':dl.enabled,'owner':dl.owner.id,'device_id':dl.device.id,'device_title':dl.device.title})
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None,devices_pk=None):
        queryset = ClockedScheduleDev.objects.filter(pk=pk, device=devices_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = ClockedScheduleDevSerializer(queryset_tmp)
        return Response(serializer.data)


class PeriodicTaskDevViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备相关的计划任务列表

    create:
    创建设备相关的计划任务

    retrieve:
    查询设备相关的计划任务详情

    update:
    更新设备相关的计划任务

    partial_update:
    更新设备相关的计划任务部分属性

    destroy:
    删除设备相关的计划任务

    """	

    serializer_class = PeriodicTaskDevSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset =PeriodicTaskDev.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
           
    def list(self, request, devices_pk=None):
        queryset = PeriodicTaskDev.objects.filter(device=devices_pk)
        # serializer = PeriodicTaskDevSerializer(queryset, many=True)
        # return Response(serializer.data)
        tmplist = []
        for dl in queryset: #('id','name','task','interval','crontab','solar','clocked','args','kwargs','queue','exchange','routing_key','priority',
            #'expires','one_off','start_time','enabled','last_run_at','total_run_count','date_changed','description','owner','device')
            scheduleplan = ''
            intervalid = ''
            cronid = ''
            clkid = ''
            if dl.interval:
                intervalid= dl.interval.id
                scheduleplan = "每隔"+str(dl.interval.every)+str(dl.interval.period)
            if dl.crontab:
                cronid = dl.crontab.id
                scheduleplan = dl.crontab.minute+" "+dl.crontab.hour+" "+dl.crontab.day_of_week+" "+dl.crontab.day_of_month+" "+dl.crontab.month_of_year
            if dl.clocked:
                clkid = dl.clocked.id
                scheduleplan = dl.clocked.clocked_time
            import json
            tmpact = json.loads(dl.kwargs)
            print(tmpact.get('http_action'))
            #print(tmpact['action'])
            try:
                if tmpact.get('http_action'):
                    gact = DeviceHttpAction.objects.get(pk=tmpact['http_action'])
                if tmpact.get('mqtt_action'):
                    gact = DeviceMqttAction.objects.get(pk=tmpact['mqtt_action'])
            except:
                pass
            tmplist.append({'id':dl.id,'name':dl.name,'task':dl.task,"action":gact.title,"scheduleplan":scheduleplan,'interval':intervalid,'crontab':cronid,'clocked':clkid,\
                'expires':dl.expires,'kwargs':dl.kwargs,'start_time':dl.start_time,'enabled':dl.enabled,'last_run_at':dl.last_run_at,'total_run_count':dl.total_run_count,'description':dl.description,'owner':dl.owner.id,'device_id':dl.device.id,'device_title':dl.device.title})
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None,devices_pk=None):
        queryset = PeriodicTaskDev.objects.filter(pk=pk, device=devices_pk)
        queryset_tmp = get_object_or_404(queryset, pk=pk)

        serializer = PeriodicTaskDevSerializer(queryset_tmp)
        return Response(serializer.data)

#device job   DeviceHttpAction,DeviceMqttAction,DeviceTriggerjobHttp,DeviceTriggerjobMqtt
class DeviceHttpActionViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备相关HTTP动作列表

    create:
    创建设备相关HTTP动作计划

    retrieve:
    查询设备相关HTTP动作详情

    update:
    更新设备相关HTTP动作

    partial_update:
    更新设备相关HTTP动作部分属性

    destroy:
    删除设备相关HTTP动作

    """

    serializer_class = DeviceHttpActionSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = DeviceHttpAction.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def list(self, request, devices_pk=None):

        queryset = DeviceHttpAction.objects.filter(device=devices_pk)

        self.check_object_permissions(request,DeviceHttpAction)
        serializer = DeviceHttpActionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, devices_pk=None):
        queryset_tmp = DeviceHttpAction.objects.get(pk=pk, device=devices_pk)
        serializer = DeviceHttpActionSerializer(queryset_tmp)
        return Response(serializer.data)

class DeviceMqttActionViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备相关MQTT动作列表

    create:
    创建设备相关MQTT动作计划

    retrieve:
    查询设备相关MQTT动作详情

    update:
    更新设备相关MQTT动作

    partial_update:
    更新设备相关MQTT动作部分属性

    destroy:
    删除设备相关MQTT动作

    """

    serializer_class = DeviceMqttActionSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = DeviceMqttAction.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def list(self, request, devices_pk=None):

        queryset = DeviceMqttAction.objects.filter(device=devices_pk)

        self.check_object_permissions(request,DeviceMqttAction)
        serializer = DeviceMqttActionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, devices_pk=None):
        queryset_tmp = DeviceMqttAction.objects.get(pk=pk, device=devices_pk)
        serializer = DeviceMqttActionSerializer(queryset_tmp)
        return Response(serializer.data)


class DeviceTriggerjobHttpViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备相关HTTP触发任务列表

    create:
    创建设备相关HTTP触发任务计划

    retrieve:
    查询设备相关HTTP触发任务详情

    update:
    更新设备相关HTTP触发任务

    partial_update:
    更新设备相关HTTP触发任务部分属性

    destroy:
    删除设备相关HTTP触发任务

    """

    serializer_class = DeviceTriggerjobHttpSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = DeviceTriggerjobHttp.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def list(self, request, devices_pk=None):

        queryset = DeviceTriggerjobHttp.objects.filter(device=devices_pk)

        # self.check_object_permissions(request,DeviceTriggerjobHttp)
        # serializer = DeviceTriggerjobHttpSerializer(queryset, many=True)
        # return Response(serializer.data)
        tmplist = []
        for dl in queryset:
            tmplist.append({'id':dl.id,'title':dl.title,'owner':dl.owner.id,'device':dl.device.title,'datachannel':dl.datachannel.id,'datachannel_title':dl.datachannel.title,'threshold_value':dl.threshold_value,'maximum':dl.maximum,'minimum':dl.minimum,'action':dl.action.id,'action_title':dl.action.title,'created':dl.created,'updated':dl.updated,'compare_choice':dl.compare_choice,'status_choice':dl.status_choice})
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None, devices_pk=None):
        queryset_tmp = DeviceTriggerjobHttp.objects.get(pk=pk, device=devices_pk)
        # serializer = DeviceTriggerjobHttpSerializer(queryset_tmp)
        # return Response(serializer.data)
        info = {'id':queryset_tmp.id,'title':queryset_tmp.title,'owner':owner,'device':queryset_tmp.device.title,'datachannel':queryset_tmp.datachannel.id,'datachannel_title':queryset_tmp.datachannel.title,'threshold_value':queryset_tmp.threshold_value,'maximum':queryset_tmp.maximum,\
            'minimum':queryset_tmp.minimum,'action':queryset_tmp.action.id,'action_title':queryset_tmp.action.title,'created':queryset_tmp.created,'updated':queryset_tmp.updated,'compare_choice':queryset_tmp.compare_choice,'status_choice':queryset_tmp.status_choice}
        return JSONResponse(info)


class DeviceTriggerjobMqttViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备相关MQTT触发任务列表

    create:
    创建设备相关MQTT触发任务计划

    retrieve:
    查询设备相关MQTT触发任务详情

    update:
    更新设备相关MQTT触发任务

    partial_update:
    更新设备相关MQTT触发任务部分属性

    destroy:
    删除设备相关MQTT触发任务

    """

    serializer_class = DeviceTriggerjobMqttSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = DeviceTriggerjobMqtt.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def list(self, request, devices_pk=None):

        queryset = DeviceTriggerjobMqtt.objects.filter(device=devices_pk)

        # self.check_object_permissions(request,DeviceTriggerjobMqtt)
        # serializer = DeviceTriggerjobMqttSerializer(queryset, many=True)
        # return Response(serializer.data)
        tmplist = []
        for dl in queryset:
            tmplist.append({'id':dl.id,'title':dl.title,'owner':dl.owner.id,'device':dl.device.title,'datachannel':dl.datachannel.id,'datachannel_title':dl.datachannel.title,'threshold_value':dl.threshold_value,'maximum':dl.maximum,'minimum':dl.minimum,'action':dl.action.id,'action_title':dl.action.title,'created':dl.created,'updated':dl.updated,'compare_choice':dl.compare_choice,'status_choice':dl.status_choice})
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None, devices_pk=None):
        queryset_tmp = DeviceTriggerjobMqtt.objects.get(pk=pk, device=devices_pk)
        # serializer = DeviceTriggerjobMqttSerializer(queryset_tmp)
        # return Response(serializer.data)
        info = {'id':queryset_tmp.id,'title':queryset_tmp.title,'owner':queryset_tmp.owner,'device':queryset_tmp.device.title,'datachannel':queryset_tmp.datachannel.id,'datachannel_title':queryset_tmp.datachannel.title,\
            'threshold_value':queryset_tmp.threshold_value,'maximum':queryset_tmp.maximum,'minimum':queryset_tmp.minimum,'action':queryset_tmp.action.id,'action_title':queryset_tmp.action.title,'created':queryset_tmp.created,\
                'updated':queryset_tmp.updated,'compare_choice':queryset_tmp.compare_choice,'status_choice':queryset_tmp.status_choice}
        return JSONResponse(info)