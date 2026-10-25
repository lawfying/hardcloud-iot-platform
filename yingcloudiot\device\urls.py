from django.urls import include, url

from rest_framework_nested import routers
from .views import DeviceViewSet,DeviceTagsViewSet,DataChannelViewSet,DataUnitViewSet,CtrlChannelViewSet,CtrlUnitViewSet,\
MetricDataViewSet,TextDataViewSet,SwitchDataViewSet,GPSDataViewSet,MeasurementViewSet,MessageViewSet,SwitchStatusViewSet,PositionViewSet\
    ,IntervalScheduleDevViewSet,CrontabScheduleDevViewSet,ClockedScheduleDevViewSet,PeriodicTaskDevViewSet,\
    DeviceHttpActionViewSet,DeviceMqttActionViewSet,DeviceTriggerjobHttpViewSet,DeviceTriggerjobMqttViewSet

from django.conf import settings
router = routers.SimpleRouter()
router.register(r'devices', DeviceViewSet,base_name='devices')
#先创建一个路由实例，再注册一个url
#第一级URL

device_router = routers.NestedSimpleRouter(router, r'devices', lookup='devices')
device_router.register(r'devicetags',DeviceTagsViewSet, base_name='devicetags' )
device_router.register(r'datachannels', DataChannelViewSet, base_name='datachannels')
device_router.register(r'ctrlchannels', CtrlChannelViewSet, base_name='ctrlchannels')

device_router.register(r'intervalscheduledev',IntervalScheduleDevViewSet, base_name='intervalscheduledev' )
device_router.register(r'crontabscheduledev',CrontabScheduleDevViewSet, base_name='crontabscheduledev' )
device_router.register(r'clockedscheduledev',ClockedScheduleDevViewSet, base_name='clockedscheduledev' )
device_router.register(r'periodictaskdev',PeriodicTaskDevViewSet, base_name='periodictaskdev' )

device_router.register(r'devicehttpactions',DeviceHttpActionViewSet, base_name='devicehttpactions' )
device_router.register(r'devicemqttactions',DeviceMqttActionViewSet, base_name='devicemqttactions' )
device_router.register(r'devicetriggerjobhttp',DeviceTriggerjobHttpViewSet, base_name='devicetriggerjobhttp' )
device_router.register(r'devicetriggerjobmqtt',DeviceTriggerjobMqttViewSet, base_name='devicetriggerjobmqtt' )
#第二级URL PeriodicTaskDev  

datachannel_router = routers.NestedSimpleRouter(device_router,r'datachannels',lookup='datachannels')
datachannel_router.register(r'dataunits',DataUnitViewSet,base_name='dataunits')
datachannel_router.register(r'measurements',MeasurementViewSet,base_name='measurements')
datachannel_router.register(r'messages',MessageViewSet,base_name='messages')
datachannel_router.register(r'switchstatus',SwitchStatusViewSet,base_name='switchstatus')
datachannel_router.register(r'position',PositionViewSet,base_name='position')
#第三级URL

ctrlchannel_router = routers.NestedSimpleRouter(device_router,r'ctrlchannels',lookup='ctrlchannels')
ctrlchannel_router.register(r'ctrlunits',CtrlUnitViewSet,base_name='ctrlunits')
ctrlchannel_router.register(r'metricdata',MetricDataViewSet,base_name='metricdata')
ctrlchannel_router.register(r'textdata',TextDataViewSet,base_name='textdata')
ctrlchannel_router.register(r'switchdata',SwitchDataViewSet,base_name='switchdata')
ctrlchannel_router.register(r'gpsdata',GPSDataViewSet,base_name='gpsdata')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(device_router.urls)),
    url(r'^', include(datachannel_router.urls)),
    url(r'^', include(ctrlchannel_router.urls)),
]