from django.contrib import admin
from .models import IotSubDev,IotSubDatachannel
# Register your models here.
class IotSubDevAdmin(admin.ModelAdmin):
    fields = ['device','device_title','owner','topic','status']
    list_display = ['id','device','device_title','owner','topic','status']

class IotSubDatachannelAdmin(admin.ModelAdmin):
    fields = ['datachannel','device_title','channel_title','owner','topic','status']
    list_display = ['id','datachannel','device_title','channel_title','owner','topic','status']

admin.site.register(IotSubDev,IotSubDevAdmin)
admin.site.register(IotSubDatachannel,IotSubDatachannelAdmin)
