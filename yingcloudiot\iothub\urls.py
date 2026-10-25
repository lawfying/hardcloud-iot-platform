from django.urls import include, url
from rest_framework_nested import routers
from .views import IotSubDevViewSet,IotSubDev2ViewSet

from django.conf import settings

router2 = routers.SimpleRouter()
router2.register(r'devices', IotSubDev2ViewSet,base_name='devices')

#先创建一个路由实例，再注册一个url
#第一级URL
from device.urls import router
iotsubdev_router = routers.NestedSimpleRouter(router, r'devices', lookup='devices')
iotsubdev_router.register(r'iotsubdevs',IotSubDevViewSet, base_name='iotsubdevs' )


urlpatterns = [
    url(r'^', include(iotsubdev_router.urls)),
    url(r'^', include(router2.urls)),
]