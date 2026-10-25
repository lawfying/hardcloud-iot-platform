from django.db import models
import locale
from django.utils.translation import gettext_lazy as _
import uuid
import mongoengine
import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from django_celery_beat.models import IntervalSchedule,CrontabSchedule,PeriodicTask,ClockedSchedule

class Device(models.Model):
    """
    设备模板表

    """
    MQTT = 'MQTT' 
    HTTP = 'HTTP'
    #CoAP = 'CoAP'
    PROTOCAL_CHOICES = (
        (MQTT, 'MQTT'),
        (HTTP, 'HTTP'),
        #(CoAP, 'CoAP'),   
    )

    ONLINE = 'ONLINE' 
    OFFLINE = 'OFFLINE'
    UNACTIVE = 'UNACTIVE'
    ACTIVE = 'ACTIVE'
    STATUS_CHOICES = (
        (ONLINE, 'ONLINE'),
        (OFFLINE, 'OFFLINE'),
        (UNACTIVE, 'UNACTIVE'),
        (ACTIVE, 'ACTIVE'),     
    )


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=80, blank=True)
    description = models.TextField(_(u"Description"), blank=True)
    img = models.ImageField(upload_to='image',default = 'upload/none.jpg', blank=True)
    device_type = models.CharField( max_length=40, blank=True)
    is_custom_registered = models.BooleanField(default=False)
    register_code = models.CharField( max_length=120, blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=UNACTIVE) 
    protocal_type = models.CharField(max_length=20,choices=PROTOCAL_CHOICES,default=HTTP) 
    last_online = models.DateTimeField(blank=True,null=True)
    activated = models.DateTimeField(blank=True,null=True)
    updated = models.DateTimeField(_(u"Updated date"), auto_now=True)
    created = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
  
    def __str__(self):  # Python 3: def __str__(self):
        return self.title


#20190907 add schedule for device
class IntervalScheduleDev(IntervalSchedule):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

class CrontabScheduleDev(CrontabSchedule):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

class ClockedScheduleDev(ClockedSchedule):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

class PeriodicTaskDev(PeriodicTask):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

@receiver(post_save, sender=PeriodicTaskDev)
def reload_celery_beat_task(sender, instance=None, created=False, **kwargs):
    try:
        #tmp = PeriodicTask.objects.get(id=2)
        tmp = PeriodicTask.objects.get(id=7)
        if tmp.enabled == True:
            tmp.enabled = False
        else:
            tmp.enabled = True
        tmp.save()
    except:
        pass

class DeviceTags(models.Model):
    """
    设备标签表，用来设置设备模板的元数据

    """
    device = models.ForeignKey(Device, on_delete=models.CASCADE)  
    key = models.CharField(max_length=80)
    value = models.CharField(max_length=200)
    
    def __str__(self):  # Python 3: def __str__(self):
        return self.key



class DataChannel(models.Model):
    """
    设备模板数据通道，数据通道是设备向云端上传数据的通道；
    上传数据通道有四种数据类型，数值型，文本型，开关型，GPS型
    """
    DECIMAL = 'DECIMAL' 
    MESSAGE = 'MESSAGE'
    SWITCH = 'SWITCH'
    GPS = 'GPS'
    DATATYPE_CHOICES = (
        (DECIMAL, '数值型'),
        (MESSAGE, '文本型'),
        (SWITCH, '开关型'),
        (GPS, 'GPS型'),    
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device = models.ForeignKey(Device,  on_delete=models.CASCADE)  
    title = models.CharField(max_length=80, blank=True)
    datatype = models.CharField(max_length=200,choices=DATATYPE_CHOICES,default=DECIMAL)
    
    def __str__(self):  # Python 3: def __str__(self):
        return self.title        


class DataUnit(models.Model):
    """
    对于上传的数据，如果是数值型，需要设置数值的单位
    """
    datachannel = models.OneToOneField(DataChannel,  on_delete=models.CASCADE)  
    unitlabel = models.CharField(max_length=20, blank=True)
    symbol = models.CharField(max_length=20, blank=True)
    max_value = models.FloatField(blank=True)
    min_value = models.FloatField(blank=True)
    step = models.FloatField(blank=True)

    def __str__(self):  # Python 3: def __str__(self):
        return self.unitlabel            


class CtrlChannel(models.Model):
    """
    设备模板的控制通道，所谓控制通道，就是云端向设备发送的指令，
    控制点接受指令而执行一系列动作；
    因此，控制通道有两个方向，一是云端发送指令，是云端到设备的控制点；
    另外是设备的控制点需要实时向云端发送自身的状态；

    """
    DECIMAL = 'DECIMAL' 
    MESSAGE = 'MESSAGE'
    SWITCH = 'SWITCH'
    GPS = 'GPS'
    DATATYPE_CHOICES = (
        (DECIMAL, '数值型'),
        (MESSAGE, '文本型'),
        (SWITCH, '开关型'),
        (GPS, 'GPS型'),    
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device = models.ForeignKey(Device,  on_delete=models.CASCADE) 
    title = models.CharField(max_length=80, blank=True)
    datatype = models.CharField(max_length=200,choices=DATATYPE_CHOICES,default=DECIMAL)
    
    def __str__(self):  # Python 3: def __str__(self):
        return self.title        


class CtrlUnit(models.Model):
    """
	控制通道的数值单位
    """
    ctrlchannel = models.OneToOneField(CtrlChannel,  on_delete=models.CASCADE)  
    unitlabel = models.CharField(max_length=20, blank=True)
    symbol = models.CharField(max_length=20, blank=True)
    max_value = models.FloatField(blank=True)
    min_value = models.FloatField(blank=True)
    step = models.FloatField(blank=True)

    def __str__(self):  # Python 3: def __str__(self):
        return self.unitlabel


class MetricData(models.Model):
    """
    控制通道的数值型数据，具有两个方向，UP表示设备上报的状态数据
    DOWN表示设备接收的控制数据
    """
    UP = 'UP' 
    DOWN = 'DOWN'
    DIRECTION_CHOICES = (
        (UP, 'UP'),
        (DOWN, 'DOWN'),   
    )

    ctrlchannel = models.ForeignKey(CtrlChannel,  on_delete=models.CASCADE)  
    value = models.FloatField(blank=True)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES,default=UP)
    timestamp = models.DateTimeField(_(u"timestamp"), auto_now_add=True)
    #只有数据变化时才更新
    # def save(self, *args, **kwargs):
    #     queryset = MetricData.objects.filter(ctrlchannel=self.ctrlchannel,direction='UP')
    #     if queryset:
    #         tmp = queryset[len(queryset)-1]
    #         if((self.value == tmp.value) and (self.direction =='UP')):
    #             pass
    #         else:
    #             super(MetricData, self).save(*args, **kwargs)
    #     else:
    #         super(MetricData, self).save(*args, **kwargs)
            

class TextData(models.Model):
    """
    控制通道的文本型数据，具有两个方向，UP表示设备上报的文本
    DOWN表示设备接收的文本信息
    """
    UP = 'UP' 
    DOWN = 'DOWN'
    DIRECTION_CHOICES = (
        (UP, 'UP'),
        (DOWN, 'DOWN'),   
    )

    ctrlchannel = models.ForeignKey(CtrlChannel,  on_delete=models.CASCADE)  
    text = models.CharField(max_length=400, blank=True)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES,default=UP)
    timestamp = models.DateTimeField(_(u"timestamp"), auto_now_add=True)
    #只有数据变化时才更新
    # def save(self, *args, **kwargs):
    #     queryset = TextData.objects.filter(ctrlchannel=self.ctrlchannel,direction='UP')
    #     if queryset:
    #         tmp = queryset[len(queryset)-1]
    #         if((self.text == tmp.text) and (self.direction =='UP')):
    #             pass
    #         else:
    #             super(TextData, self).save(*args, **kwargs)
    #     else:
    #         super(TextData, self).save(*args, **kwargs)

class SwitchData(models.Model):
    """
    控制通道的开关型数据，具有两个方向，UP表示设备上报的开关状态
    DOWN表示设备接收的开关控制
    """
    UP = 'UP' 
    DOWN = 'DOWN'
    DIRECTION_CHOICES = (
        (UP, 'UP'),
        (DOWN, 'DOWN'),   
    )

    ctrlchannel = models.ForeignKey(CtrlChannel,  on_delete=models.CASCADE)  
    switch = models.BooleanField(blank=True)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES,default=UP)
    timestamp = models.DateTimeField(_(u"timestamp"), auto_now_add=True)
    #只有数据变化时才更新
    # def save(self, *args, **kwargs):
    #     queryset = SwitchData.objects.filter(ctrlchannel=self.ctrlchannel,direction='UP')
    #     if queryset:
    #         tmp = queryset[len(queryset)-1]
    #         if((self.switch == tmp.switch) and (self.direction =='UP')):
    #             pass
    #         else:
    #             super(SwitchData, self).save(*args, **kwargs)
    #     else:
    #         super(SwitchData, self).save(*args, **kwargs)

class GPSData(models.Model):
    """
    控制通道的GPS型数据，具有两个方向，UP表示设备上报的GPS数据
    DOWN表示设备接收的GPS数据
    """
    UP = 'UP' 
    DOWN = 'DOWN'
    DIRECTION_CHOICES = (
        (UP, 'UP'),
        (DOWN, 'DOWN'),   
    )

    ctrlchannel = models.ForeignKey(CtrlChannel,  on_delete=models.CASCADE)  
    longitude = models.FloatField(blank=True)
    latitude = models.FloatField(blank=True)
    elevation = models.FloatField(blank=True)
    address = models.CharField(max_length=400, blank=True)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES,default=UP)
    timestamp = models.DateTimeField(_(u"timestamp"), auto_now_add=True)
    
    #只有数据变化时才更新
    # def save(self, *args, **kwargs):
    #     queryset = GPSData.objects.filter(ctrlchannel=self.ctrlchannel,direction='UP')
    #     if queryset:
    #         tmp = queryset[0]
    #         if((self.longitude == tmp.longitude and self.latitude == tmp.latitude) and (self.direction =='UP')):
    #             pass
    #         else:
    #             super(GPSData, self).save(*args, **kwargs)
    #     else:
    #         super(GPSData, self).save(*args, **kwargs)

#mongodb document
class Measurement(mongoengine.Document):
    datachannel = mongoengine.UUIDField(binary=False, required=True)
    timestamp = mongoengine.DateTimeField()
    value = mongoengine.FloatField()
    meta = {
        'indexes': [
            'datachannel',
            '$datachannel',  # text index
            '#datachannel',  # hashed index
            {
                'fields': ['timestamp'],
                'expireAfterSeconds': 15552000 #180 day 
            }
        ]
    }


# from trigger.tasks import globalhttptask

# @receiver(post_save, sender=SwitchData)
# def globalhttptask1(sender,  **kwargs):
#     globalhttptask(sig_action="1")

#触发任务，判断
from trigger.tasks import signal_triggernew,trigger_http_task,trigger_mqtt_task
from trigger.models import TriggerjobNew,GlobalHttpAction,GlobalMqttAction,TriggerjobNewMqtt,IntervalScheduleNew,\
    CrontabScheduleNew,PeriodicTaskNew,ClockedScheduleNew

from mongoengine import signals as msignals

from django.db import transaction

@receiver(post_save, sender=IntervalScheduleDev)
def create_global_interval(sender, instance=None, created=False, **kwargs):
    if created:
        tmp = IntervalScheduleNew(id=instance.id,every=instance.every,period=instance.period,owner=instance.owner)
        tmp.save()

@receiver(post_save, sender=ClockedScheduleDev)
def create_global_clocked(sender, instance=None, created=False, **kwargs):
    if created:
        tmp = ClockedScheduleNew(id=instance.id,clocked_time=instance.clocked_time,enabled=instance.enabled,owner=instance.owner)
        tmp.save()

@receiver(post_save, sender=CrontabScheduleDev)
def create_global_crons(sender, instance=None, created=False, **kwargs):
    if created:
        tmp = CrontabScheduleNew(id=instance.id,minute=instance.minute,hour=instance.hour,day_of_week=instance.day_of_week,\
            day_of_month=instance.day_of_month,month_of_year=instance.month_of_year,owner=instance.owner)
        tmp.save()

@receiver(post_save, sender=PeriodicTaskDev)
def create_global_task(sender, instance=None, created=False, **kwargs):
    if created:
        tmp = PeriodicTaskNew(id=instance.id,name=instance.name,task=instance.task,interval=instance.interval,\
            crontab=instance.crontab,solar=instance.solar,clocked=instance.clocked,args=instance.args,kwargs=instance.kwargs,\
            expires=instance.expires,one_off=instance.one_off,start_time=instance.start_time,enabled=instance.enabled,last_run_at=instance.last_run_at,\
                description=instance.description,owner=instance.owner)
        tmp.save()

@receiver(msignals.post_save, sender=Measurement)
def trigger_http_job(sender, document=None, **kwargs):
    print('http task pre')
    try:
        trigger_http_task(document)
        print('trigger http task ok!')
    except:
        pass
    try:
        trigger_mqtt_task(document)
        print('trigger mqtt task ok!')
    except:
        pass
    return True


class Message(mongoengine.Document):
    datachannel = mongoengine.UUIDField(binary=False, required=True)
    timestamp = mongoengine.DateTimeField()
    message = mongoengine.StringField(max_length=400)
    meta = {
        'indexes': [
            'datachannel',
            '$datachannel',  # text index
            '#datachannel',  # hashed index
            {
                'fields': ['timestamp'],
                'expireAfterSeconds': 15552000 #180 day
            }
        ]
    }

class SwitchStatus(mongoengine.Document):
    datachannel = mongoengine.UUIDField(binary=False, required=True)
    timestamp = mongoengine.DateTimeField()
    status = mongoengine.BooleanField()
    meta = {
        'indexes': [
            'datachannel',
            '$datachannel',  # text index
            '#datachannel',  # hashed index
            {
                'fields': ['timestamp'],
                'expireAfterSeconds': 15552000 #180 day
            }
        ]
    }

class Position(mongoengine.Document):
    datachannel = mongoengine.UUIDField(binary=False, required=True)
    timestamp = mongoengine.DateTimeField()
    latitude = mongoengine.FloatField()
    longitude = mongoengine.FloatField()
    elevation = mongoengine.FloatField()
    address = mongoengine.StringField(max_length=400)
    meta = {
        'indexes': [
            'datachannel',
            '$datachannel',  # text index
            '#datachannel',  # hashed index
            {
                'fields': ['timestamp'],
                'expireAfterSeconds': 15552000 #180 day
            }
        ]
    }

#from trigger.models import TriggerjobNew,GlobalHttpAction,GlobalMqttAction,TriggerjobNewMqtt
class DeviceHttpAction(GlobalHttpAction):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

class DeviceMqttAction(GlobalMqttAction):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

class DeviceTriggerjobHttp(TriggerjobNew):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

class DeviceTriggerjobMqtt(TriggerjobNewMqtt):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

#2022-12-11增加功能：设备如有第一次接收或者发送数据，设备的状态就改为 ACTIVE

@receiver(post_save, sender=MetricData)
@receiver(post_save, sender=TextData)
@receiver(post_save, sender=GPSData)
@receiver(post_save, sender=SwitchData)
def update_device_active(sender, instance=None, created=False, **kwargs):
    try:
        if created:
            tmp = Device.objects.get(id=instance.ctrlchannel.device.id)
            if (tmp.status != 'ACTIVE'):
                tmp.status = 'ACTIVE'
                tmp.save()
            else:
                pass
    except:
        pass


@receiver(msignals.post_save, sender=Measurement)
@receiver(msignals.post_save, sender=Message)
@receiver(msignals.post_save, sender=SwitchStatus)
@receiver(msignals.post_save, sender=Position)
def update_device_active2(sender, document=None, **kwargs):
    try:
        tmp1 = DataChannel.objects.filter(id=document.datachannel)
        tmp2 = Device.objects.get(id=tmp1[0].device.id)
        if (tmp2.status != 'ACTIVE'):
            tmp2.status = 'ACTIVE'
            tmp2.save()
        else:
            pass
    except:
        pass