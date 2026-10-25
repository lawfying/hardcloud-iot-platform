from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt import authentication
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import action

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


from django.shortcuts import get_object_or_404 
import datetime
from accounts.models import DevHolder,ScenarioHolder
from device.models import Device,DataChannel,CtrlChannel
from scenario.models import Scenario


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view()
def dashboard_num(request):
    devtmp = DevHolder.objects.filter(binding_dev__owner=request.user)
    devholder_num = devtmp.count()
    now_time = datetime.datetime.now()
    num_1mon = DevHolder.objects.filter(binding_dev__owner=request.user,bonding_date__month=now_time.month).count()
    num_2mon = DevHolder.objects.filter(binding_dev__owner=request.user,bonding_date__month=(now_time.month-1)).count()
    num_3mon = DevHolder.objects.filter(binding_dev__owner=request.user,bonding_date__month=(now_time.month-2)).count()
    num_4mon = DevHolder.objects.filter(binding_dev__owner=request.user,bonding_date__month=(now_time.month-3)).count()
    num_5mon = DevHolder.objects.filter(binding_dev__owner=request.user,bonding_date__month=(now_time.month-4)).count()

    scetmp = ScenarioHolder.objects.filter(binding_sce__owner=request.user)
    sceholder_num = scetmp.count()
    num_1mon_sce = ScenarioHolder.objects.filter(binding_sce__owner=request.user,bonding_date__month=now_time.month).count()
    num_2mon_sce = ScenarioHolder.objects.filter(binding_sce__owner=request.user,bonding_date__month=(now_time.month-1)).count()
    num_3mon_sce = ScenarioHolder.objects.filter(binding_sce__owner=request.user,bonding_date__month=(now_time.month-2)).count()
    num_4mon_sce = ScenarioHolder.objects.filter(binding_sce__owner=request.user,bonding_date__month=(now_time.month-3)).count()
    num_5mon_sce = ScenarioHolder.objects.filter(binding_sce__owner=request.user,bonding_date__month=(now_time.month-4)).count()

    devtmp = Device.objects.filter(owner=request.user)
    dev_num = devtmp.count()
    dev_num_active = Device.objects.filter(owner=request.user,status='ACTIVE',created__month=now_time.month).count()
    num_1mon_dev = Device.objects.filter(owner=request.user,created__month=now_time.month).count()
    num_2mon_dev = Device.objects.filter(owner=request.user,created__month=(now_time.month-1)).count()
    num_3mon_dev = Device.objects.filter(owner=request.user,created__month=(now_time.month-2)).count()
    num_4mon_dev = Device.objects.filter(owner=request.user,created__month=(now_time.month-3)).count()
    num_5mon_dev = Device.objects.filter(owner=request.user,created__month=(now_time.month-4)).count()

    sceapptmp = Scenario.objects.filter(owner=request.user)
    sceapp_num = sceapptmp.count()
    num_1mon_sceapp = Scenario.objects.filter(owner=request.user,created__month=now_time.month).count()
    num_2mon_sceapp = Scenario.objects.filter(owner=request.user,created__month=(now_time.month-1)).count()
    num_3mon_sceapp = Scenario.objects.filter(owner=request.user,created__month=(now_time.month-2)).count()
    num_4mon_sceapp = Scenario.objects.filter(owner=request.user,created__month=(now_time.month-3)).count()
    num_5mon_sceapp = Scenario.objects.filter(owner=request.user,created__month=(now_time.month-4)).count()

    dchtmp = DataChannel.objects.filter(device__owner=request.user)
    dch_num = dchtmp.count()
    cchtmp = CtrlChannel.objects.filter(device__owner=request.user)
    cch_num = cchtmp.count()

    info = {'num':devholder_num,'last5mon':[num_5mon,num_4mon,num_3mon,num_2mon,num_1mon],\
        'sce_num':sceholder_num,'sce_last5mon':[num_5mon_sce,num_4mon_sce,num_3mon_sce,num_2mon_sce,num_1mon_sce],\
            'dev_num':dev_num,'dev_num_active':dev_num_active,'dev_last5mon':[num_5mon_dev,num_4mon_dev,num_3mon_dev,num_2mon_dev,num_1mon_dev],\
                'sceapp_num':sceapp_num,'sceapp_last5mon':[num_5mon_sceapp,num_4mon_sceapp,num_3mon_sceapp,num_2mon_sceapp,num_1mon_sceapp],\
                    'dch_num':dch_num,'cch_num':cch_num}
    return JSONResponse(info)