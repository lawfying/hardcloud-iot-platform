from django.contrib import admin
from .models import DevTemplate,TemplateTags,TplDataChannel,TplDataUnit,TplCtrlChannel,TplCtrlUnit

class DevTemplateAdmin(admin.ModelAdmin):
    fields = ['title', 'description','img','device_type','is_custom_registered','protocal_type','owner']
    list_display = ['id','title', 'description','img','device_type','is_custom_registered','protocal_type','owner','updated','created']

class TemplateTagsAdmin(admin.ModelAdmin):
	"""docstring for Cat"""
	fields = ['devtemplate', 'key', 'value']
	list_display = ['id','devtemplate', 'key', 'value']


class TplDataChannelAdmin(admin.ModelAdmin):

	fields = ['devtemplate', 'title', 'datatype']
	list_display = ['id','devtemplate', 'title', 'datatype']		


class TplDataUnitAdmin(admin.ModelAdmin):

	fields = ['tpldatachannel', 'unitlabel', 'symbol', 'max_value', 'min_value', 'step']
	list_display = ['id','tpldatachannel', 'unitlabel', 'symbol', 'max_value', 'min_value', 'step']	

class TplCtrlChannelAdmin(admin.ModelAdmin):

	fields = ['devtemplate', 'title', 'datatype']
	list_display = ['id','devtemplate', 'title', 'datatype']		


class TplCtrlUnitAdmin(admin.ModelAdmin):

	fields = ['tplctrlchannel', 'unitlabel', 'symbol', 'max_value', 'min_value', 'step']
	list_display = ['id','tplctrlchannel', 'unitlabel', 'symbol', 'max_value', 'min_value', 'step']	



admin.site.register(DevTemplate,DevTemplateAdmin)
admin.site.register(TemplateTags,TemplateTagsAdmin)

admin.site.register(TplDataChannel,TplDataChannelAdmin)
admin.site.register(TplDataUnit,TplDataUnitAdmin)
admin.site.register(TplCtrlChannel,TplCtrlChannelAdmin)
admin.site.register(TplCtrlUnit,TplCtrlUnitAdmin)
