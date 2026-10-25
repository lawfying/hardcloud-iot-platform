from django.shortcuts import render
from .serializers import MyProfileSerializer,DevHolderSerializer,ScenarioHolderSerializer
from .models import MyProfile,DevHolder,ScenarioHolder
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt import authentication
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework.decorators import action

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status

from device.models import Device
from scenario.models import Scenario
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404 
from device.models import DataChannel,Message,CtrlChannel,TextData,Measurement,MetricData,SwitchData,SwitchStatus,GPSData,Position,Device
from device.serializers import MessageSerializer,TextDataSerializer,MeasurementSerializer,MetricDataSerializer,SwitchDataSerializer,SwitchStatusSerializer,GPSDataSerializer,PositionSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class  MyProfileViewSet(viewsets.ModelViewSet):
    """
    list:
    查询个人信息列表

    create:
    创建个人信息

    retrieve:
    查询个人信息详情

    update:
    更新个人信息

    partial_update:
    更新个人信息部分属性

    destroy:
    删除个人信息

    """

    serializer_class =  MyProfileSerializer

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)

    queryset =  MyProfile.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
           
    def list(self, request,):
        queryset = MyProfile.objects.filter(user=request.user)
        qs = queryset[0]
        # serializer = MyProfileSerializer(queryset, many=True)
        # return Response(serializer.data)
        info = {'myprofile_id':qs.id,'user_id':qs.user.id,'username':qs.user.username,'email':qs.user.email,'phone_num':qs.phone_num,'mugshot':'/media/'+str(qs.mugshot)}
        return JSONResponse(info)

    def retrieve(self, request, pk=None):
        queryset = MyProfile.objects.filter(user=request.user)
        myprofile = get_object_or_404(queryset, pk=pk)
        serializer = MyProfileSerializer(myprofile)
        return Response(serializer.data)


class  DevHolderViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备持有者列表

    create:
    创建设备持有者，用户使用者绑定设备，返回详细信息

    retrieve:
    查询设备持有者详情

    update:
    更新设备持有者

    partial_update:
    更新设备持有者部分属性

    destroy:
    删除设备持有者

    dev_accesstoken:
    获取设备访问token(使用者获取设备创建者的access token)，id为设备的id

    holddevlist:
    使用者直接获取绑定的设备列表，包括了设备名称，持有人姓名

    holddevmessages:
    所有绑定设备的最新一条上传message，用于APP消息首页

    holddevallmessages：
    所绑定设备的所有消息通道的最新值
    
    holddevallgps：
    所绑定设备的所有GPS通道的最新值，格式'channel_type':'ctrl','data_type':'DECIMAL','channel_title':cch.title,'upload_value':msg['value'],'download_value':msg2['value'],'devid':dev.id,'channel_id':cch.id

    holddevalldecimal：
    所绑定设备的所有数值通道的最新值，格式'channel_type':'ctrl','data_type':'DECIMAL','channel_title':cch.title,'upload_value':msg['value'],'download_value':msg2['value'],'devid':dev.id,'channel_id':cch.id

    holddevallswitch：
    所绑定设备的所有开关通道的最新值，格式'channel_type':'ctrl','data_type':'DECIMAL','channel_title':cch.title,'upload_value':msg['value'],'download_value':msg2['value'],'devid':dev.id,'channel_id':cch.id
    """

    serializer_class =  DevHolderSerializer

    permission_classes = (permissions.IsAuthenticated,)
    #authentication_classes = (BasicAuthentication,)
    authentication_classes = (authentication.JWTAuthentication,)

    queryset = DevHolder.objects.all()

    #如果是管理员admin绑定，就需要根据提交的表单，如果是普通用户绑定，就是绑定到自己
    def perform_create(self, serializer):
        if(str(self.request.user)=="admin"):
            print(self.request.data['dev_owner'])
            holder = User.objects.get(pk=self.request.data['dev_owner'])
            serializer.save(dev_owner=holder)
        else:
            serializer.save(dev_owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        #优化思路：创建完成之后返回详细结果数据，可以考虑self.perform_create(serializer)的返回值,就不需要下面的查询
        dev = DevHolder.objects.get(pk=serializer.data['id'])
        info = {'holder':dev.dev_owner.username,'holddevice':dev.binding_dev.title,'holddeviceimg':str(dev.binding_dev.img),'holddevicestatus':dev.binding_dev.status,'holddevid':dev.binding_dev.id,'holddate':dev.bonding_date}
        return Response(info, status=status.HTTP_201_CREATED, headers=headers)
        
    def list(self, request,):
        #queryset = DevHolder.objects.filter(dev_owner=request.user)
        #Book.objects.select_related('author__hometown').get(id=4)
        queryset = DevHolder.objects.filter(binding_dev__owner=request.user)
        serializer = DevHolderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = DevHolder.objects.filter(dev_owner=request.user)
        myprofile = get_object_or_404(queryset, pk=pk)
        serializer = DevHolderSerializer(myprofile)
        return Response(serializer.data)

    #通过设备的使用者来获取访问设备的的token，使用者需要通过设备创建者的access token才能访问接口资源
    #下面接口的思路：首先根据设备id查询到该设备，然后查询该设备是否和使用者绑定，如果绑定就获取创建者的access token
    @action(detail=True, methods=['get'])
    def dev_accesstoken(self, request, pk=None):
        # devtmp = Device.objects.get(pk=pk)
        # queryset = DevHolder.objects.get(binding_dev=devtmp,dev_owner=request.user)
        # tokentmp = AccessToken()
        # tokentmp = tokentmp.for_user(user=queryset.dev_owner)
        # info = {'accesstoken':str(tokentmp),'devid':pk}
        # 2021-04-07 修改，进行结果判断
        try:
            devtmp = Device.objects.get(pk=pk)
            queryset = DevHolder.objects.get(binding_dev=devtmp,dev_owner=request.user)
            tokentmp = AccessToken()
            tokentmp = tokentmp.for_user(user=devtmp.owner)
            info = {'accesstoken':str(tokentmp),'devid':pk}
        except:
            info = {'exception'}

        return JSONResponse(info)

    @list_route(methods=['get'])
    def holddevlist(self, request,):
        #设备使用人查看设备被用户绑定的情况
        queryset = DevHolder.objects.filter(dev_owner=request.user)
        # queryset2 = Device.objects.filter(owner=request.user)
        infolist=[]
        for dev in queryset:
            #print(dev.binding_dev.title)
            # devtmp = Device.objects.get(pk=queryset.binding_dev.id)
            # devuser = User.objects.get(pk=queryset.dev_owner.id)
            info = {'holder':dev.dev_owner.username,'holddevice':dev.binding_dev.title,'holddeviceimg':str(dev.binding_dev.img),'holddevicestatus':dev.binding_dev.status,'holddevid':dev.binding_dev.id,'holddate':dev.bonding_date}
            infolist.append(info)
        # for dev2 in queryset2:
        #     #print(dev.binding_dev.title)
        #     # devtmp = Device.objects.get(pk=queryset.binding_dev.id)
        #     # devuser = User.objects.get(pk=queryset.dev_owner.id)
        #     info2 = {'holder':dev2.owner.username,'holddevice':dev2.title,'holddeviceimg':str(dev2.img),'holddevicestatus':dev2.status,'holddevid':dev2.id,'holddate':dev2.created}
        #     infolist.append(info2)
        return JSONResponse(infolist)

       #获取所有绑定设备的最新上传消息
    @list_route(methods=['get'])
    def holddevmessages(self, request,):
        queryset = DevHolder.objects.filter(dev_owner=request.user)
        infolist=[]
        for dev in queryset:
            datachs_list = DataChannel.objects.filter(device=dev.binding_dev,datatype='MESSAGE')
            for dch in datachs_list:
                msgobj =  Message.objects(datachannel=dch.id)
                serializer = MessageSerializer(msgobj, many=True)
                msg = serializer.data
                if msg != []:
                    msg = msg[-1]
                    info = {'holddevice':dch.device.title,'datachannel':dch.title,'holddeviceimg':str(dch.device.img),'message':msg['message'],'timestamp':msg['timestamp']}
                    infolist.append(info)
                else:
                    pass
        return JSONResponse(infolist)


    #查询绑定设备的所有数值通道的最新数据值
    @list_route(methods=['post'])
    def holddevalldecimal(self, request,):
        infolist=[]
        try:
            dev = Device.objects.get(pk=request.data['devid'])
            datachs_list = DataChannel.objects.filter(device=dev,datatype='DECIMAL')
            ctrlchs_list = CtrlChannel.objects.filter(device=dev,datatype='DECIMAL')
            for dch in datachs_list:
                msgobj =  Measurement.objects(datachannel=dch.id)
                serializer = MeasurementSerializer(msgobj, many=True)
                msg = serializer.data
                if msg != []:
                    msg = msg[-1]
                    info = {'channel_type':'data','data_type':'DECIMAL','channel_title':dch.title,'upload_value':msg['value'],'download_value':'','devid':dev.id,'channel_id':dch.id}
                    infolist.append(info)
                else:
                    pass

            for cch in ctrlchs_list:
                msgobj =  MetricData.objects.filter(ctrlchannel=cch.id,direction='UP').order_by('-timestamp')
                serializer = MetricDataSerializer(msgobj, many=True)
                msg = serializer.data

                msgobj2 =  MetricData.objects.filter(ctrlchannel=cch.id,direction='DOWN').order_by('-timestamp')
                serializer2 = MetricDataSerializer(msgobj, many=True)
                msg2 = serializer2.data

                if msg != [] or msg2 !=[]:
                    msg = msg[0]
                    msg2 = msg2[0]
                    info = {'channel_type':'ctrl','data_type':'DECIMAL','channel_title':cch.title,'upload_value':msg['value'],'download_value':msg2['value'],'devid':dev.id,'channel_id':cch.id}
                    infolist.append(info)
                else:
                    pass
        except:
            pass
        return JSONResponse(infolist)


    #查询绑定设备的所有开关通道的最新数据值
    @list_route(methods=['post'])
    def holddevallswitch(self, request,):
        infolist=[]
        try:
            dev = Device.objects.get(pk=request.data['devid'])
            datachs_list = DataChannel.objects.filter(device=dev,datatype='SWITCH')
            ctrlchs_list = CtrlChannel.objects.filter(device=dev,datatype='SWITCH')
            for dch in datachs_list:
                msgobj =  SwitchStatus.objects(datachannel=dch.id)
                serializer = SwitchStatusSerializer(msgobj, many=True)
                msg = serializer.data
                if msg != []:
                    msg = msg[-1]
                    info = {'channel_type':'data','data_type':'SWITCH','channel_title':dch.title,'upload_value':msg['status'],'download_value':'','devid':dev.id,'channel_id':dch.id}
                    infolist.append(info)
                else:
                    pass

            for cch in ctrlchs_list:
                msgobj =  SwitchData.objects.filter(ctrlchannel=cch.id,direction='UP').order_by('-timestamp')
                serializer = SwitchDataSerializer(msgobj, many=True)
                msg = serializer.data

                msgobj2 =  SwitchData.objects.filter(ctrlchannel=cch.id,direction='DOWN').order_by('-timestamp')
                serializer2 = SwitchDataSerializer(msgobj, many=True)
                msg2 = serializer2.data

                if msg != [] or msg2 != []:
                    msg = msg[0]
                    msg2 = msg2[0]
                    info = {'channel_type':'ctrl','data_type':'SWITCH','channel_title':cch.title,'upload_value':msg['switch'],'download_value':msg2['switch'],'devid':dev.id,'channel_id':cch.id}
                    infolist.append(info)
                else:
                    pass
            
        except:
            pass
        return JSONResponse(infolist)

    #查询绑定设备的所有消息通道的最新数据值
    @list_route(methods=['post'])
    def holddevallmessages(self, request,):
        infolist=[]
        try:
            dev = Device.objects.get(pk=request.data['devid'])
            datachs_list = DataChannel.objects.filter(device=dev,datatype='MESSAGE')
            ctrlchs_list = CtrlChannel.objects.filter(device=dev,datatype='MESSAGE')
            for dch in datachs_list:
                msgobj =  Message.objects(datachannel=dch.id)
                serializer = MessageSerializer(msgobj, many=True)
                msg = serializer.data
                if msg != []:
                    msg = msg[-1]
                    info = {'channel_type':'data','data_type':'MESSAGE','channel_title':dch.title,'upload_value':msg['message'],'download_value':'','devid':dev.id,'channel_id':dch.id}
                    infolist.append(info)
                else:
                    pass

            for cch in ctrlchs_list:
                msgobj =  TextData.objects.filter(ctrlchannel=cch.id,direction='UP').order_by('-timestamp')
                serializer = TextDataSerializer(msgobj, many=True)
                msg = serializer.data

                msgobj2 =  TextData.objects.filter(ctrlchannel=cch.id,direction='DOWN').order_by('-timestamp')
                serializer2 = TextDataSerializer(msgobj2, many=True)
                msg2 = serializer2.data

                if msg != [] or msg2 != []:
                    msg = msg[0]
                    msg2 = msg2[0]
                    info = {'channel_type':'ctrl','data_type':'MESSAGE','channel_title':cch.title,'upload_value':msg['text'],'download_value':msg2['text'],'devid':dev.id,'channel_id':cch.id}
                    infolist.append(info)
                else:
                    pass
            
        except:
            pass
        return JSONResponse(infolist)

    #查询绑定设备的所有GPS通道的最新数据值
    @list_route(methods=['post'])
    def holddevallgps(self, request,):
        infolist=[]
        try:
            dev = Device.objects.get(pk=request.data['devid'])
            datachs_list = DataChannel.objects.filter(device=dev,datatype='GPS')
            ctrlchs_list = CtrlChannel.objects.filter(device=dev,datatype='GPS')
            for dch in datachs_list:
                msgobj =  Position.objects(datachannel=dch.id)
                serializer = PositionSerializer(msgobj, many=True)
                msg = serializer.data
                if msg != []:
                    msg = msg[-1]
                    info = {'channel_type':'data','data_type':'GPS','channel_title':dch.title,'upload_value':msg['address'],'download_value':'','devid':dev.id,'channel_id':dch.id}
                    infolist.append(info)
                else:
                    pass

            for cch in ctrlchs_list:
                msgobj =  GPSData.objects.filter(ctrlchannel=cch.id,direction='UP').order_by('-timestamp')
                serializer = GPSDataSerializer(msgobj, many=True)
                msg = serializer.data

                msgobj2 =  GPSData.objects.filter(ctrlchannel=cch.id,direction='DOWN').order_by('-timestamp')
                serializer2 = GPSDataSerializer(msgobj2, many=True)
                msg2 = serializer2.data

                if msg != [] or msg2 !=[]:
                    msg = msg[0]
                    msg2 = msg2[0]
                    info = {'channel_type':'ctrl','data_type':'GPS','channel_title':cch.title,'upload_value':msg['address'],'download_value':msg2['address'],'devid':dev.id,'channel_id':cch.id}
                    infolist.append(info)
                else:
                    pass
        except:
            pass
        return JSONResponse(infolist)

class  ScenarioHolderViewSet(viewsets.ModelViewSet):
    """
    list:
    查询应用场景持有者列表

    create:
    创建应用场景持有者

    retrieve:
    查询应用场景持有者详情

    update:
    更新应用场景持有者

    partial_update:
    更新应用场景持有者部分属性

    destroy:
    删除应用场景持有者

    sce_accesstoken:
    获取应用场景访问token,id为场景的id

    """

    serializer_class =  ScenarioHolderSerializer

    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    #authentication_classes = (BasicAuthentication,)
    authentication_classes = (authentication.JWTAuthentication,)

    queryset = ScenarioHolder.objects.all()
           
    def list(self, request,):
        queryset = ScenarioHolder.objects.filter(binding_sce__owner=request.user)
        # queryset2 = Scenario.objects.filter(owner=request.user)
        # serializer = ScenarioHolderSerializer(queryset, many=True)
        # return Response(serializer.data)
        tmplist = []
        for dl in queryset:
            tmplist.append({"id":dl.id,"sce_owner":dl.sce_owner.username,"binding_sce":dl.binding_sce.id,"bonding_date":dl.bonding_date,"binding_sce_title":dl.binding_sce.title})
        # for dl2 in queryset2:
        #     tmplist.append({"id":dl2.id,"sce_owner":dl2.owner.username,"binding_sce":dl2.id,"bonding_date":dl2.created,"binding_sce_title":dl2.title})
        return JSONResponse(tmplist)

    def retrieve(self, request, pk=None):
        queryset = ScenarioHolder.objects.filter(sce_owner=request.user)
        myprofile = get_object_or_404(queryset, pk=pk)
        serializer = ScenarioHolderSerializer(myprofile)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def sce_accesstoken(self, request, pk=None):
        scetmp = Scenario.objects.get(pk=pk)
        queryset = ScenarioHolder.objects.get(binding_sce=scetmp,sce_owner=request.user)
        tokentmp = AccessToken()
        tokentmp = tokentmp.for_user(user=queryset.sce_owner)
        info = {'accesstoken':str(tokentmp)}

        return JSONResponse(info)