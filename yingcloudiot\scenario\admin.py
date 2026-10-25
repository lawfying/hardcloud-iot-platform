from django.contrib import admin
from .models import Scenario,Collection,DevLink,CtrlSetting,LinkCtrlChannel,CtrlChannelParam

class ScenarioAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['title','description','img','owner']
    list_display = ['id','title','description','img','owner','updated','created']  

class CollectionAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['title','description','scenario']
    list_display = ['id','title','description','scenario','updated','created']  

class DevLinkAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['device','collection','owner']
    list_display = ['id','device','collection','date_joined','owner']  

class CtrlSettingAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['title','description','collection']
    list_display = ['id','title','description','collection']  

class LinkCtrlChannelAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['ctrlsetting','ctrlchannel','owner']
    list_display = ['id','ctrlsetting','ctrlchannel','owner']  

class CtrlChannelParamAdmin(admin.ModelAdmin):
    """docstring for Cat"""
    fields = ['linkctrlchannel','key','value']
    list_display = ['id','linkctrlchannel','key','value']  

admin.site.register(Scenario,ScenarioAdmin)
admin.site.register(Collection,CollectionAdmin)
admin.site.register(DevLink,DevLinkAdmin)
admin.site.register(CtrlSetting,CtrlSettingAdmin)
admin.site.register(LinkCtrlChannel,LinkCtrlChannelAdmin)
admin.site.register(CtrlChannelParam,CtrlChannelParamAdmin)
