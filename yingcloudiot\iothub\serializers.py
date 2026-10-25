from django.forms import widgets
from rest_framework import serializers
from rest_framework.relations import RelatedField
from .models import IotSubDev,IotSubDatachannel
class IotSubDevSerializer(serializers.ModelSerializer):

    class Meta:
        model = IotSubDev
        fields = ('id','device','device_title','owner','topic','status')