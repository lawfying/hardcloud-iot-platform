from django.db import models
import locale
from django.utils.translation import gettext_lazy as _
import uuid
from device.models import Device,DataChannel

from django.db.models.signals import post_save
from django.dispatch import receiver

from django_celery_beat.models import IntervalSchedule,SolarSchedule,CrontabSchedule,PeriodicTask,ClockedSchedule

class IntervalScheduleNew(IntervalSchedule):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class CrontabScheduleNew(CrontabSchedule):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class ClockedScheduleNew(ClockedSchedule):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class PeriodicTaskNew(PeriodicTask):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

@receiver(post_save, sender=PeriodicTaskNew)
def reload_celery_beat_task(sender, instance=None, created=False, **kwargs):
    try:
        #tmp = PeriodicTask.objects.get(id=2)
        tmp = PeriodicTask.objects.get(name="celery.backend_cleanup")
        if tmp.enabled == True:
            tmp.enabled = False
        else:
            tmp.enabled = True
        tmp.save()
    except:
        pass

#20190830 add global celery action

class GlobalHttpAction(models.Model):
    """
        Action is 
        :param pktoken: Primary key automatically produced by system

    """

    title = models.CharField(_(u"Title"), help_text=_(u"A descriptive name for the Action."), max_length=80, blank=True)
    description = models.TextField(_(u"Description"), blank=True)
    url = models.URLField(max_length=400,blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    updated = models.DateTimeField(_(u"Updated date"), auto_now=True) 
    

    def __str__(self): # Python 3: def __str__(self):
        return self.title

class HttpKeyvalue(models.Model):
    key = models.CharField(_(u"key"),max_length=20, blank=True)
    value =  models.CharField(_(u"value"),max_length=400, blank=True)
    action =  models.ForeignKey(GlobalHttpAction,on_delete=models.CASCADE)


class GlobalMqttAction(models.Model):
    """
        Action is 
        :param pktoken: Primary key automatically produced by system

    """

    title = models.CharField(_(u"Title"), help_text=_(u"A descriptive name for the Action."), max_length=80, blank=True)
    description = models.TextField(_(u"Description"), blank=True)
    topic = models.CharField(_(u"topic"),max_length=40, blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    updated = models.DateTimeField(_(u"Updated date"), auto_now=True) 
    

    def __str__(self): # Python 3: def __str__(self):
        return self.title

class MqttKeyvalue(models.Model):
    key = models.CharField(_(u"key"),max_length=20, blank=True)
    value =  models.CharField(_(u"value"),max_length=400, blank=True)
    action =  models.ForeignKey(GlobalMqttAction,on_delete=models.CASCADE)

#新的触发任务，与全局HTTP动作相关
class TriggerjobNew(models.Model):
    """
        Trigger is 
        :param pktoken: Primary key automatically produced by system

    """
    GREAT_THAN= 'GREAT_THAN'
    EQUAL = 'EQUAL'
    GREAT_EQUAL = 'GREAT_EQUAL'
    LITTLE_THAN = 'LITTLE_THAN'
    LITTLE_EQUAL = 'LITTLE_EQUAL'
    BETWEEN_MAX_MIN = 'BETWEEN_MAX_MIN'
    NOT_BETWEEN_MAX_MIN = 'NOT_BETWEEN_MAX_MIN'
    COMPARE_CHOICES = (
        (GREAT_THAN,'Great than threshold value'),
        (EQUAL, 'Equal threshold value'),
        (GREAT_EQUAL,'Great and equal threshold value'),
        (LITTLE_THAN, 'Little than threshold value'),     
        (LITTLE_EQUAL, 'Little and equal threshold value'),  
        (BETWEEN_MAX_MIN, 'Between Maximum and Minimum'),
        (NOT_BETWEEN_MAX_MIN, 'Not Between Maximum and Minimum'),                      
    )

    RUNNING = 'RUNNING'
    PAUSING = 'PAUSING'
    STATUS_CHOICES = (
        (RUNNING, 'RUNNING'),
        (PAUSING, 'PAUSING'),
    )

    title = models.CharField(_(u"Title"), help_text=_(u"A descriptive name for the Action."), max_length=80, blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datachannel = models.ForeignKey(DataChannel, on_delete=models.CASCADE) 
    threshold_value = models.CharField(blank=True,max_length=10)
    maximum = models.CharField(blank=True,max_length=10,default="100")
    minimum = models.CharField(blank=True,max_length=10,default="0")
    action =  models.ForeignKey(GlobalHttpAction, on_delete=models.CASCADE) 
    created = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    updated = models.DateTimeField(_(u"Updated date"), auto_now=True)       
    compare_choice =  models.CharField(
        max_length=20,
        choices=COMPARE_CHOICES,
        default=EQUAL,
    )
    status_choice =  models.CharField(
        max_length=10,
        choices=STATUS_CHOICES, 
        default=PAUSING,
    )  
  
    def __str__(self):  # Python 3: def __str__(self):
        return self.title

#新的触发任务，与全局HTTP动作相关
class TriggerjobNewMqtt(models.Model):
    """
        Trigger is 
        :param pktoken: Primary key automatically produced by system

    """
    GREAT_THAN= 'GREAT_THAN'
    EQUAL = 'EQUAL'
    GREAT_EQUAL = 'GREAT_EQUAL'
    LITTLE_THAN = 'LITTLE_THAN'
    LITTLE_EQUAL = 'LITTLE_EQUAL'
    BETWEEN_MAX_MIN = 'BETWEEN_MAX_MIN'
    NOT_BETWEEN_MAX_MIN = 'NOT_BETWEEN_MAX_MIN'
    COMPARE_CHOICES = (
        (GREAT_THAN,'Great than threshold value'),
        (EQUAL, 'Equal threshold value'),
        (GREAT_EQUAL,'Great and equal threshold value'),
        (LITTLE_THAN, 'Little than threshold value'),     
        (LITTLE_EQUAL, 'Little and equal threshold value'),  
        (BETWEEN_MAX_MIN, 'Between Maximum and Minimum'),
        (NOT_BETWEEN_MAX_MIN, 'Not Between Maximum and Minimum'),                      
    )

    RUNNING = 'RUNNING'
    PAUSING = 'PAUSING'
    STATUS_CHOICES = (
        (RUNNING, 'RUNNING'),
        (PAUSING, 'PAUSING'),
    )

    title = models.CharField(_(u"Title"), help_text=_(u"A descriptive name for the Action."), max_length=80, blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datachannel = models.ForeignKey(DataChannel, on_delete=models.CASCADE) 
    threshold_value = models.CharField(blank=True,max_length=10)
    maximum = models.CharField(blank=True,max_length=10,default="100")
    minimum = models.CharField(blank=True,max_length=10,default="0")
    action =  models.ForeignKey(GlobalMqttAction, on_delete=models.CASCADE) 
    created = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    updated = models.DateTimeField(_(u"Updated date"), auto_now=True)       
    compare_choice =  models.CharField(
        max_length=20,
        choices=COMPARE_CHOICES,
        default=EQUAL,
    )
    status_choice =  models.CharField(
        max_length=10,
        choices=STATUS_CHOICES, 
        default=PAUSING,
    )  
  
    def __str__(self):  # Python 3: def __str__(self):
        return self.title