from django.urls import include, url
#from django.urls import path
from django.urls import path

from rest_framework_nested import routers
from .views import testglobalhttpaction,TriggerjobNewViewSet,TriggerjobNewMqttViewSet

from .views_beat import IntervalScheduleViewSet_Beat,SolarScheduleViewSet_Beat,CrontabScheduleViewSet_Beat,PeriodicTaskViewSet_Beat,\
    ClockedScheduleViewSet_Beat,GlobalHttpActionViewSet_Beat,HttpKeyvalueViewSet_Beat,GlobalMqttActionViewSet_Beat,MqttKeyvalueViewSet_Beat,\
        IntervalScheduleTopViewSet_Beat,SolarScheduleTopViewSet_Beat,CrontabScheduleTopViewSet_Beat,PeriodicTaskTopViewSet_Beat,ClockedScheduleTopViewSet_Beat

from django.conf import settings

#先创建一个路由实例，再注册一个url
#第一级URL
from device.urls import router


job_router = routers.SimpleRouter()
job_router.register(r'triggerhttpjobs', TriggerjobNewViewSet,base_name='triggerhttpjobs')
job_router.register(r'triggermqttjobs', TriggerjobNewMqttViewSet,base_name='triggermqttjobs')


beat_router = routers.SimpleRouter()
beat_router.register(r'intervals', IntervalScheduleViewSet_Beat,base_name='intervals')
beat_router.register(r'solars', SolarScheduleViewSet_Beat,base_name='solars')
beat_router.register(r'crons', CrontabScheduleViewSet_Beat,base_name='crons')
beat_router.register(r'periodtask', PeriodicTaskViewSet_Beat,base_name='periodtask')
beat_router.register(r'clocked', ClockedScheduleViewSet_Beat,base_name='clocked')

beat_router.register(r'globalhttpaction', GlobalHttpActionViewSet_Beat,base_name='globalhttpaction')
globalhttpaction_router = routers.NestedSimpleRouter(beat_router, r'globalhttpaction', lookup='globalhttpaction')
globalhttpaction_router.register(r'httpkeyvalue',HttpKeyvalueViewSet_Beat, base_name='httpkeyvalue' )

beat_router.register(r'globalmqttaction', GlobalMqttActionViewSet_Beat,base_name='globalmqttaction')
globalmqttaction_router = routers.NestedSimpleRouter(beat_router, r'globalmqttaction', lookup='globalmqttaction')
globalmqttaction_router.register(r'mqttkeyvalue',MqttKeyvalueViewSet_Beat, base_name='mqttkeyvalue' )
#先创建一个路由实例，再注册一个url ClockedScheduleViewSet_Beat
#第一级URL ClockedScheduleTopViewSet_Beat
beat_router_top = routers.SimpleRouter()
beat_router_top.register(r'intervals_top', IntervalScheduleTopViewSet_Beat,base_name='intervals_top')
beat_router_top.register(r'solars_top', SolarScheduleTopViewSet_Beat,base_name='solars_top')
beat_router_top.register(r'crons_top', CrontabScheduleTopViewSet_Beat,base_name='crons_top')
beat_router_top.register(r'clocked_top', ClockedScheduleTopViewSet_Beat,base_name='clocked_top')
beat_router_top.register(r'periodtask_top', PeriodicTaskTopViewSet_Beat,base_name='periodtask_top')

urlpatterns = [
    url(r'^', include(job_router.urls)),
    url(r'^', include(beat_router.urls)),
    url(r'^', include(globalhttpaction_router.urls)),
    url(r'^', include(globalmqttaction_router.urls)),
    path('globalhttpactions/<int:pk>/status',testglobalhttpaction),
    url(r'^', include(beat_router_top.urls)),
]