from .models import MyProfile,DevHolder,ScenarioHolder
from rest_framework import serializers
from django.contrib.auth.models import User

class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProfile
        fields = ('user','phone_num', 'mugshot')


class DevHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevHolder
        fields = ('id','dev_owner','binding_dev','bonding_date','user_dev_bind')

class ScenarioHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenarioHolder
        fields = ('id','sce_owner','binding_sce','bonding_date','user_sce_bind')
