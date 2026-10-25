from django.db import models
import locale
from django.utils.translation import gettext_lazy as _
import uuid

#设备模板模块，主要是预定义设备的原型，包括设备的属性，数据点，控制点，及其传输通道
#设备模块应用模块，包括了一下数据库表：
#设备模板表、设备模板标签表、设备模板数据通道表、数据通道单位表、设备模板控制通道表，
#控制通道数值单位表；


class DevTemplate(models.Model):
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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField( max_length=80, blank=True)
    description = models.TextField(_(u"Description"), blank=True)
    img = models.ImageField(upload_to='image',default = 'upload/none.jpg', blank=True)
    device_type = models.CharField( max_length=40, blank=True)
    is_custom_registered = models.BooleanField(default=False)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    protocal_type = models.CharField(max_length=200,choices=PROTOCAL_CHOICES,default=HTTP) 
    updated = models.DateTimeField(_(u"Updated date"), auto_now=True)
    created = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    
  
    def __str__(self):  # Python 3: def __str__(self):
        return self.title


class TemplateTags(models.Model):
    """
    设备模板标签表，用来设置设备模板的元数据

    """
    devtemplate = models.ForeignKey(DevTemplate, on_delete=models.CASCADE)  
    key = models.CharField(max_length=80)
    value = models.CharField(max_length=200)
    
    def __str__(self):  # Python 3: def __str__(self):
        return self.key



class TplDataChannel(models.Model):
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

    devtemplate = models.ForeignKey(DevTemplate,  on_delete=models.CASCADE)  
    title = models.CharField(max_length=80, blank=True)
    datatype = models.CharField(max_length=200,choices=DATATYPE_CHOICES,default=DECIMAL)
    
    def __str__(self):  # Python 3: def __str__(self):
        return self.title        


class TplDataUnit(models.Model):
    """
    对于上传的数据，如果是数值型，需要设置数值的单位;下面需要修改，是一对一关系
    """
    tpldatachannel = models.OneToOneField(TplDataChannel, on_delete=models.CASCADE)  
    unitlabel = models.CharField(max_length=20, blank=True)
    symbol = models.CharField(max_length=20, blank=True)
    max_value = models.FloatField(blank=True)
    min_value = models.FloatField(blank=True)
    step = models.FloatField(blank=True)

    def __str__(self):  # Python 3: def __str__(self):
        return self.unitlabel            


class TplCtrlChannel(models.Model):
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

    devtemplate = models.ForeignKey(DevTemplate,  on_delete=models.CASCADE) 
    title = models.CharField(max_length=80, blank=True)
    datatype = models.CharField(max_length=200,choices=DATATYPE_CHOICES,default=DECIMAL)
    
    def __str__(self):  # Python 3: def __str__(self):
        return self.title        


class TplCtrlUnit(models.Model):
    """
	控制通道的数值单位
    """
    tplctrlchannel = models.OneToOneField(TplCtrlChannel,  on_delete=models.CASCADE)  
    unitlabel = models.CharField(max_length=20, blank=True)
    symbol = models.CharField(max_length=20, blank=True)
    max_value = models.FloatField(blank=True)
    min_value = models.FloatField(blank=True)
    step = models.FloatField(blank=True)

    def __str__(self):  # Python 3: def __str__(self):
        return self.unitlabel 