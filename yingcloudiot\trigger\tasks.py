from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .celery import app
from .models import GlobalHttpAction,HttpKeyvalue,TriggerjobNew,GlobalMqttAction,MqttKeyvalue,TriggerjobNewMqtt
import urllib
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from django.contrib.auth.models import Permission, User
from django.conf import settings
import paho.mqtt.publish as publish

from devtemplate.models import TemplateTags,TplCtrlChannel,TplCtrlUnit,TplDataChannel,TplDataUnit,DevTemplate
from device.models import DeviceTags,CtrlChannel,CtrlUnit,DataChannel,DataUnit,Device,DataChannel

#全局计划任务
@app.task
def globalhttptask(http_action=None):
    act = GlobalHttpAction.objects.get(pk=http_action)
    keyvalue = HttpKeyvalue.objects.filter(action=act)

    paras_data = {}
    for paras_tmp in keyvalue:
        paras_data[paras_tmp.key] = paras_tmp.value

    tokentmp = AccessToken()
    tokentmp = tokentmp.for_user(user=act.owner)

    import urllib.parse
    import urllib.request
    import json

    token = 'Bearer'+' '+str(tokentmp)
    headers = {'Authorization':token}
    
    url = act.url
    data = urllib.parse.urlencode(paras_data).encode('utf-8')
    print(data)
    req=urllib.request.Request(url=url,data=data,headers=headers,method = 'POST')
    response = urllib.request.urlopen(req)
    data = response.read().decode("utf-8",'ignore')
    print("test ok")
    return True

#全局计划任务
@app.task
def globalmqtttask(mqtt_action=None):
    act = GlobalMqttAction.objects.get(pk=mqtt_action)
    keyvalue = MqttKeyvalue.objects.filter(action=act)

    paras_data = {}
    for paras_tmp in keyvalue:
        paras_data[paras_tmp.key] = paras_tmp.value
    # 2019 ADD USER
    #publish.single(act.topic, paras_data, hostname=settings.MQTT_HOST,auth={'username':settings.MQTT_USERNAME,'password':settings.MQTT_PASSWORD})
    publish.single(act.topic, str(paras_data), hostname=settings.MQTT_HOST)

    print("test ok-mqtt")
    return True


#当根据模板创建设备时，异步任务创建相关的标签、通道
@app.task
def createByTemplatetask(device_args=None,template_args=None):
    device = Device.objects.get(id=device_args)
    template = DevTemplate.objects.get(id=template_args)
    #tags
    try:
        tpltags = TemplateTags.objects.filter(devtemplate=template)
        for tmptag in tpltags:
            devtag = DeviceTags(device=device,key=tmptag.key,value=tmptag.value)
            devtag.save()
    except:
        pass
    try:
        #the following is copy control channel
        tplcch = TplCtrlChannel.objects.filter(devtemplate=template)
        for tmptplcch in tplcch:
            ctrlch = CtrlChannel(device=device,title=tmptplcch.title, datatype=tmptplcch.datatype)
            ctrlch.save()
            if (ctrlch.datatype == 'DECIMAL'):
                try:
                    tplunit = TplCtrlUnit.objects.get(tplctrlchannel=tmptplcch)
                    ctrlunit = CtrlUnit(ctrlchannel=ctrlch,unitlabel=tplunit.unitlabel,symbol=tplunit.symbol,max_value=tplunit.max_value,min_value=tplunit.min_value,step=tplunit.step)
                    ctrlunit.save()
                except:
                    pass
            else:
                pass
    except:
        pass

    try:
        #data channel
        tpldch = TplDataChannel.objects.filter(devtemplate=template)
        for tmptpldch in tpldch:
            # copy data channel
            datach = DataChannel(device=device,title= tmptpldch.title, datatype=tmptpldch.datatype)
            datach.save()
            # if datatype is decimal,copy the data unit.
            if datach.datatype == 'DECIMAL':
                try:
                    tplunit = TplDataUnit.objects.get(tpldatachannel=tmptpldch)
                    dataunit = DataUnit(datachannel=datach,unitlabel=tplunit.unitlabel,symbol=tplunit.symbol,max_value=tplunit.max_value,min_value=tplunit.min_value,step=tplunit.step)
                    dataunit.save()
                except:
                    pass
            else:
                pass
    except:
        pass
    return True

@app.task
def trigger_http_task(document=None):
    try:
        print("test222")
        dc = document.datachannel
        #print("test222")
        value = document.value
        #print("test222")
        triggerlist = TriggerjobNew.objects.filter(datachannel=dc)
        for trigger in triggerlist:
            #print(trigger)
            action = trigger.action.id
            #print(action)
            #print(trigger.status_choice)
            
            if trigger.status_choice == "RUNNING":
                #发出一个任务
                threshold = float(trigger.threshold_value)
                maximum = float(trigger.maximum)
                minimum = float(trigger.minimum)

                if trigger.compare_choice == 'GREAT_THAN':
                    if value > threshold:
                        signal_triggernew(sig_action=action)
                elif  trigger.compare_choice == 'EQUAL':
                    if value == threshold:
                        signal_triggernew(sig_action=action)
                elif  trigger.compare_choice == 'GREAT_EQUAL': 
                    if value >= threshold:
                        signal_triggernew(sig_action=action)
                elif  trigger.compare_choice == 'LITTLE_THAN':
                    if value < threshold:
                        signal_triggernew(sig_action=action)
                elif  trigger.compare_choice == 'LITTLE_EQUAL':
                    if value <= threshold:
                        signal_triggernew(sig_action=action)
                elif  trigger.compare_choice == 'BETWEEN_MAX_MIN':
                    if value <= maximum and value >= minimum:
                        signal_triggernew(sig_action=action)
                elif  trigger.compare_choice == 'NOT_BETWEEN_MAX_MIN':
                    if value > maximum or value < minimum:
                        signal_triggernew(sig_action=action)
                else:
                    pass

            #signal_trigger(sig_action=action,sig_ds=dc,sig_vl=value)
    except:
        pass


@app.task
def trigger_mqtt_task(document=None):
    try:
        print("test222")
        dc = str(document.datachannel)
        #print("test222")
        value = document.value
        print(dc)
        triggerlist = TriggerjobNewMqtt.objects.filter(datachannel=dc)
        for trigger in triggerlist:
            print("trigger")
            action = trigger.action.id
            print(action)
            print(trigger.status_choice)
            
            if trigger.status_choice == "RUNNING":
                #发出一个任务
                threshold = float(trigger.threshold_value)
                maximum = float(trigger.maximum)
                minimum = float(trigger.minimum)

                if trigger.compare_choice == 'GREAT_THAN':
                    if value > threshold:
                        globalmqtttask(mqtt_action=action)
                elif  trigger.compare_choice == 'EQUAL':
                    if value == threshold:
                        globalmqtttask(mqtt_action=action)
                elif  trigger.compare_choice == 'GREAT_EQUAL': 
                    if value >= threshold:
                        globalmqtttask(mqtt_action=action)
                elif  trigger.compare_choice == 'LITTLE_THAN':
                    if value < threshold:
                        globalmqtttask(mqtt_action=action)
                elif  trigger.compare_choice == 'LITTLE_EQUAL':
                    if value <= threshold:
                        globalmqtttask(mqtt_action=action)
                elif  trigger.compare_choice == 'BETWEEN_MAX_MIN':
                    if value <= maximum and value >= minimum:
                        globalmqtttask(mqtt_action=action)
                elif  trigger.compare_choice == 'NOT_BETWEEN_MAX_MIN':
                    if value > maximum or value < minimum:
                        globalmqtttask(mqtt_action=action)
                else:
                    pass

            #signal_trigger(sig_action=action,sig_ds=dc,sig_vl=value)
    except:
        pass

def signal_triggernew(sig_action=None):
    act = GlobalHttpAction.objects.get(pk=sig_action)
    keyvalue = HttpKeyvalue.objects.filter(action=act)
    #keyvalue可能是字典，也可能是列表
    paras_data = {}
    for paras_tmp in keyvalue:
        paras_data[paras_tmp.key] = paras_tmp.value

    tokentmp = AccessToken()
    tokentmp = tokentmp.for_user(user=act.owner)

    import urllib.parse
    import urllib.request
    import json

    token = 'Bearer'+' '+str(tokentmp)
    headers = {'Authorization':token}

    url = act.url
    data = urllib.parse.urlencode(paras_data).encode('utf-8')
    req=urllib.request.Request(url=url,data=data,headers=headers,method = 'POST')
    response = urllib.request.urlopen(req)
    data = response.read().decode("utf-8",'ignore')

    print("test ok")
    return True

