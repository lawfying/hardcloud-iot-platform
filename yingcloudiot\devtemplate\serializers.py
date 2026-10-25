from django.forms import widgets
from rest_framework import serializers
from rest_framework.relations import RelatedField
from .models import DevTemplate,TemplateTags,TplDataChannel,TplDataUnit,TplCtrlChannel,TplCtrlUnit

class DevTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DevTemplate
        fields = ('id', 'title', 'description','img','device_type','is_custom_registered','protocal_type','updated','created')

class TemplateTagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TemplateTags
        fields = ('id','devtemplate', 'key', 'value')

class TplDataChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TplDataChannel
        fields = ('id','devtemplate', 'title', 'datatype')

class TplDataUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = TplDataUnit
        fields = ('id','tpldatachannel', 'unitlabel', 'symbol','max_value','min_value','step')

class TplCtrlChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TplCtrlChannel
        fields = ('id','devtemplate', 'title', 'datatype')

class TplCtrlUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = TplCtrlUnit
        fields = ('id','tplctrlchannel', 'unitlabel', 'symbol','max_value','min_value','step')