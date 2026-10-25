from django.forms import widgets
from rest_framework import serializers
from rest_framework.relations import RelatedField
from .models import TriggerjobNew,TriggerjobNewMqtt

class TriggerjobNewSerializer(serializers.ModelSerializer):

    class Meta:
        model = TriggerjobNew
        fields = ('id','title','owner','datachannel','threshold_value','maximum','minimum','action','created','updated','compare_choice','status_choice')  

class TriggerjobNewMqttSerializer(serializers.ModelSerializer):

    class Meta:
        model = TriggerjobNewMqtt
        fields = ('id','title','owner','datachannel','threshold_value','maximum','minimum','action','created','updated','compare_choice','status_choice')        