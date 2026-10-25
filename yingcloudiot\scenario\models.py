from django.db import models
import locale
from django.utils.translation import gettext_lazy as _
import uuid
from device.models import Device,CtrlChannel

class Scenario(models.Model):
    """
    应用场景

    """
    title = models.CharField(max_length=80, blank=True)
    description = models.TextField(_(u"Description"), blank=True)
    img = models.ImageField(upload_to='image',default = 'upload/none.jpg', blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    updated = models.DateTimeField(_(u"Updated date"), auto_now=True)
    created = models.DateTimeField(_(u"Creation date"), auto_now_add=True) 
  
    def __str__(self):  # Python 3: def __str__(self):
        return self.title

class Collection(models.Model):
    """
    设备组

    """
    title = models.CharField(max_length=80, blank=True)
    description = models.TextField(_(u"Description"), blank=True)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)  
    devices = models.ManyToManyField(Device, through='Devlink')
    updated = models.DateTimeField(_(u"Updated date"), auto_now=True)
    created = models.DateTimeField(_(u"Creation date"), auto_now_add=True) 
  
    def __str__(self):  # Python 3: def __str__(self):
        return self.title

class DevLink(models.Model):
    """
    设备与设备组关系

    """
    device = models.ForeignKey(Device,unique=True,on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class CtrlSetting(models.Model):
    """
    设备组合设置表

    """

    title = models.CharField(max_length=80, blank=True)
    description = models.TextField(_(u"Description"), blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):  # Python 3: def __str__(self):
        return self.title

class LinkCtrlChannel(models.Model):
    """
    设置与控制通道关系表

    """
    ctrlsetting = models.ForeignKey(CtrlSetting, on_delete=models.CASCADE)
    ctrlchannel = models.ForeignKey(CtrlChannel, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):  # Python 3: def __str__(self):
        return str(self.ctrlchannel.title)


class CtrlChannelParam(models.Model):
    """
    设置与孔子通道关系表

    """
    linkctrlchannel = models.ForeignKey(LinkCtrlChannel, on_delete=models.CASCADE)
    key = models.CharField(max_length=80)
    value = models.CharField(max_length=200)

    def __str__(self):  # Python 3: def __str__(self):
        return str(self.linkctrlchannel.ctrlchannel)

