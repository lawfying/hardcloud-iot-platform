from django.contrib import admin

# Register your models here.

from .models import MyProfile,DevHolder,ScenarioHolder

class MyProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'phone_num','mugshot','is_developer','is_custom_user']
    list_display = ['id','user', 'phone_num','mugshot','is_developer','is_custom_user']

class DevHolderAdmin(admin.ModelAdmin):
    fields = ['dev_owner','binding_dev','user_dev_bind']
    list_display = ['id','dev_owner','binding_dev','bonding_date','user_dev_bind']

class ScenarioHolderAdmin(admin.ModelAdmin):
    fields = ['sce_owner','binding_sce','user_sce_bind']
    list_display = ['id','sce_owner','binding_sce','bonding_date','user_sce_bind']

admin.site.register(MyProfile,MyProfileAdmin)
admin.site.register(DevHolder,DevHolderAdmin)
admin.site.register(ScenarioHolder,ScenarioHolderAdmin)