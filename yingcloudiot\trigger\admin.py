from django.contrib import admin
from .models import GlobalHttpAction,HttpKeyvalue,GlobalMqttAction,MqttKeyvalue,\
        IntervalScheduleNew,CrontabScheduleNew,ClockedScheduleNew,PeriodicTaskNew,TriggerjobNew,TriggerjobNewMqtt


# Register your models here.

class GlobalHttpActionAdmin(admin.ModelAdmin):
    fields = ['title','description','owner','url']
    list_display = ['id','title','description','owner','url','created','updated']	

class HttpKeyvalueAdmin(admin.ModelAdmin):
    fields = ['key','value','action']
    list_display = ['id','key','value','action']

class GlobalMqttActionAdmin(admin.ModelAdmin):
    fields = ['title','description','owner','topic']
    list_display = ['id','title','description','owner','topic','created','updated']	

class MqttKeyvalueAdmin(admin.ModelAdmin):
    fields = ['key','value','action']
    list_display = ['id','key','value','action']


admin.site.register(GlobalHttpAction,GlobalHttpActionAdmin)
admin.site.register(HttpKeyvalue,HttpKeyvalueAdmin)
admin.site.register(GlobalMqttAction,GlobalMqttActionAdmin)
admin.site.register(MqttKeyvalue,MqttKeyvalueAdmin)

admin.site.register(IntervalScheduleNew)
admin.site.register(CrontabScheduleNew)
admin.site.register(ClockedScheduleNew)
admin.site.register(PeriodicTaskNew)

admin.site.register(TriggerjobNew)
admin.site.register(TriggerjobNewMqtt)