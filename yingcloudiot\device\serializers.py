from django.forms import widgets
from rest_framework import serializers
from rest_framework.relations import RelatedField
from .models import Device,DeviceTags,DataChannel,DataUnit,CtrlChannel,CtrlUnit,MetricData,TextData,SwitchData,GPSData,\
    IntervalScheduleDev,CrontabScheduleDev,ClockedScheduleDev,PeriodicTaskDev,\
        DeviceHttpAction,DeviceMqttAction,DeviceTriggerjobHttp,DeviceTriggerjobMqtt

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ('id','title', 'description','img','device_type','is_custom_registered','register_code','status','protocal_type','last_online','activated','owner','updated','created')

class DeviceTagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceTags
        fields = ('id','device', 'key', 'value')

class DataChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataChannel
        fields = ('id','device', 'title', 'datatype')

class DataUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataUnit
        fields = ('id','datachannel', 'unitlabel', 'symbol', 'max_value', 'min_value', 'step')

class CtrlChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CtrlChannel
        fields = ('id','device', 'title', 'datatype')

class CtrlUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = CtrlUnit
        fields = ('id','ctrlchannel', 'unitlabel', 'symbol', 'max_value', 'min_value', 'step')

class MetricDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetricData
        fields = ('id','ctrlchannel', 'value', 'direction', 'timestamp')

class TextDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextData
        fields = ('id','ctrlchannel', 'text', 'direction', 'timestamp')

class SwitchDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SwitchData
        fields = ('id','ctrlchannel', 'switch', 'direction', 'timestamp')

class GPSDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = GPSData
        fields = ('id','ctrlchannel', 'longitude','latitude','elevation','address', 'direction', 'timestamp')


# serializer for Datapoint in mongodb
# Measurement
class MeasurementSerializer(serializers.Serializer):
    datachannel = serializers.UUIDField(format='hex_verbose')
    timestamp =serializers.DateTimeField()
    value = serializers.FloatField()

class MessageSerializer(serializers.Serializer):
    datachannel = serializers.UUIDField(format='hex_verbose')
    timestamp =serializers.DateTimeField()
    message = serializers.CharField(max_length=400)

class SwitchStatusSerializer(serializers.Serializer):
    datachannel = serializers.UUIDField(format='hex_verbose')
    timestamp =serializers.DateTimeField()
    status = serializers.BooleanField()

class PositionSerializer(serializers.Serializer):
    datachannel = serializers.UUIDField(format='hex_verbose')
    timestamp =serializers.DateTimeField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    elevation = serializers.FloatField()
    address = serializers.CharField(max_length=400)


class IntervalScheduleDevSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntervalScheduleDev
        fields = ('id','every','period','owner','device')

class ClockedScheduleDevSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClockedScheduleDev
        fields = ('id','clocked_time','enabled','owner','device')


class CrontabScheduleDevSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrontabScheduleDev
        fields = ('id','minute','hour','day_of_week','day_of_month','month_of_year','owner','device')

class PeriodicTaskDevSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeriodicTaskDev
        fields = ('id','name','task','interval','crontab','solar','clocked','args','kwargs','queue','exchange','routing_key','priority','expires','one_off','start_time','enabled','last_run_at','total_run_count','date_changed','description','owner','device')
#DeviceHttpAction,DeviceMqttAction,DeviceTriggerjobHttp,DeviceTriggerjobMqtt

class DeviceHttpActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceHttpAction
        fields = ('id','title','description','owner','url','created','updated','device')

class DeviceMqttActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceMqttAction
        fields = ('id','title','description','owner','topic','created','updated','device')

class DeviceTriggerjobHttpSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceTriggerjobHttp
        fields = ('id','title','owner','datachannel','threshold_value','maximum','minimum','action','created','updated','compare_choice','status_choice','device')  

class DeviceTriggerjobMqttSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceTriggerjobMqtt
        fields = ('id','title','owner','datachannel','threshold_value','maximum','minimum','action','created','updated','compare_choice','status_choice','device')  