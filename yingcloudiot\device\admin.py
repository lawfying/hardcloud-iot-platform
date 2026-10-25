from django.contrib import admin
from .models import Device,DeviceTags,DataChannel,DataUnit,CtrlChannel,CtrlUnit,MetricData,TextData,SwitchData,GPSData,\
    IntervalScheduleDev,CrontabScheduleDev,ClockedScheduleDev,PeriodicTaskDev,\
        DeviceHttpAction,DeviceMqttAction,DeviceTriggerjobHttp,DeviceTriggerjobMqtt
class DeviceAdmin(admin.ModelAdmin):
    fields = ['title', 'description','img','device_type','is_custom_registered','register_code','status','protocal_type','last_online','activated','owner']
    list_display = ['id','title', 'description','img','device_type','is_custom_registered','register_code','status','protocal_type','last_online','activated','owner','updated','created']

class DeviceTagsAdmin(admin.ModelAdmin):
	"""docstring for Cat"""
	fields = ['device', 'key', 'value']
	list_display = ['id','device', 'key', 'value']

class DataChannelAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['device', 'title', 'datatype']
    list_display = ['id','device', 'title', 'datatype']     


class DataUnitAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['datachannel', 'unitlabel', 'symbol', 'max_value', 'min_value', 'step']
    list_display = ['id','datachannel', 'unitlabel', 'symbol', 'max_value', 'min_value', 'step']    

class CtrlChannelAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['device', 'title', 'datatype']
    list_display = ['id','device', 'title', 'datatype']     


class CtrlUnitAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['ctrlchannel', 'unitlabel', 'symbol', 'max_value', 'min_value', 'step']
    list_display = ['id','ctrlchannel', 'unitlabel', 'symbol', 'max_value', 'min_value', 'step']    

class MetricDataAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['ctrlchannel', 'value', 'direction']
    list_display = ['id','ctrlchannel', 'value', 'direction', 'timestamp']

class TextDataAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['ctrlchannel', 'text', 'direction']
    list_display = ['id','ctrlchannel', 'text', 'direction', 'timestamp']

class SwitchDataAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['ctrlchannel', 'switch', 'direction']
    list_display = ['id','ctrlchannel', 'switch', 'direction', 'timestamp']

class GPSDataAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['ctrlchannel', 'longitude','latitude','elevation','address', 'direction']
    list_display = ['id','ctrlchannel', 'longitude','latitude','elevation','address', 'direction', 'timestamp']

admin.site.register(Device,DeviceAdmin)
admin.site.register(DeviceTags,DeviceTagsAdmin)

admin.site.register(DataChannel,DataChannelAdmin)
admin.site.register(DataUnit,DataUnitAdmin)
admin.site.register(CtrlChannel,CtrlChannelAdmin)
admin.site.register(CtrlUnit,CtrlUnitAdmin)

admin.site.register(MetricData,MetricDataAdmin)
admin.site.register(TextData,TextDataAdmin)
admin.site.register(SwitchData,SwitchDataAdmin)
admin.site.register(GPSData,GPSDataAdmin)

admin.site.register(IntervalScheduleDev)
admin.site.register(CrontabScheduleDev)
admin.site.register(ClockedScheduleDev)
admin.site.register(PeriodicTaskDev)

admin.site.register(DeviceHttpAction)
admin.site.register(DeviceMqttAction)
admin.site.register(DeviceTriggerjobHttp)
admin.site.register(DeviceTriggerjobMqtt)

