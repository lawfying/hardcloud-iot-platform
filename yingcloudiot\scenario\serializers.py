from django.forms import widgets
from rest_framework import serializers
from rest_framework.relations import RelatedField
from .models import Scenario,Collection,DevLink,CtrlSetting,LinkCtrlChannel,CtrlChannelParam

class ScenarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scenario
        fields = ('id','title','description','img','owner','updated','created')

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('id','title','description','scenario','updated','created')

class DevLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = DevLink
        fields = ('id','device','collection','date_joined','owner')

class CtrlSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CtrlSetting
        fields = ('id','title','description','collection')

class LinkCtrlChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = LinkCtrlChannel
        fields = ('id','ctrlsetting','ctrlchannel','owner')

class CtrlChannelParamSerializer(serializers.ModelSerializer):

    class Meta:
        model = CtrlChannelParam
        fields = ('id','linkctrlchannel','key','value')