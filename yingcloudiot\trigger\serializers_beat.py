from django.forms import widgets
from rest_framework import serializers
from rest_framework.relations import RelatedField
from django_celery_beat.models import IntervalSchedule,SolarSchedule,CrontabSchedule,PeriodicTask,ClockedSchedule
from .models import GlobalHttpAction,HttpKeyvalue,GlobalMqttAction,MqttKeyvalue,\
    IntervalScheduleNew,CrontabScheduleNew,PeriodicTaskNew,ClockedScheduleNew

class IntervalScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntervalScheduleNew
        fields = ('id','every','period','owner')

class ClockedScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClockedScheduleNew
        fields = ('id','clocked_time','enabled','owner')

class SolarScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SolarSchedule
        fields = ('id','event','latitude','longitude')

class CrontabScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrontabScheduleNew
        fields = ('id','minute','hour','day_of_week','day_of_month','month_of_year','owner')

class PeriodicTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeriodicTaskNew
        fields = ('id','name','task','interval','crontab','solar','clocked','args','kwargs','queue','exchange','routing_key','priority','expires','one_off','start_time','enabled','last_run_at','total_run_count','date_changed','description','owner')

class GlobalHttpActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = GlobalHttpAction
        fields = ('id','title','description','owner','url','created','updated')

class HttpKeyvalueSerializer(serializers.ModelSerializer):

    class Meta:
        model = HttpKeyvalue
        fields = ('id','key','value','action')    

class GlobalMqttActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = GlobalMqttAction
        fields = ('id','title','description','owner','topic','created','updated')

class MqttKeyvalueSerializer(serializers.ModelSerializer):

    class Meta:
        model = MqttKeyvalue
        fields = ('id','key','value','action')    

class IntervalScheduleTopSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntervalSchedule
        fields = ('id','every','period')

class SolarScheduleTopSerializer(serializers.ModelSerializer):

    class Meta:
        model = SolarSchedule
        fields = ('id','event','latitude','longitude')

class CrontabScheduleTopSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrontabSchedule
        fields = ('id','minute','hour','day_of_week','day_of_month','month_of_year','timezone')

class ClockedScheduleTopSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClockedSchedule
        fields = ('id','clocked_time','enabled')

class PeriodicTaskTopSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeriodicTask
        fields = ('id','name','task','crontab','solar','args','kwargs','queue','exchange','routing_key','priority','expires','one_off','start_time','enabled','last_run_at','total_run_count','date_changed','description')