from django.conf.urls import include, url

from rest_framework_nested import routers
from .views import ScenarioViewSet,CollectionViewSet,DevLinkViewSet,CtrlSettingViewSet,LinkCtrlChannelViewSet,\
CtrlChannelParamViewSet
from django.conf import settings
router = routers.SimpleRouter()
router.register(r'scenarios', ScenarioViewSet,base_name='scenarios')
router.register(r'linkctrlchannels', LinkCtrlChannelViewSet,base_name='linkctrlchannels')
#先创建一个路由实例，再注册一个url
#第一级URL

scenario_router = routers.NestedSimpleRouter(router, r'scenarios', lookup='scenarios')
scenario_router.register(r'collections',CollectionViewSet, base_name='collections' )

collection_router = routers.NestedSimpleRouter(scenario_router,r'collections',lookup='collections')
collection_router.register(r'ctrlsettings',CtrlSettingViewSet,base_name='ctrlsettings')
collection_router.register(r'devlinks',DevLinkViewSet,base_name='devlinks')

linkctrlchannel_router = routers.NestedSimpleRouter(router, r'linkctrlchannels', lookup='linkctrlchannels')
linkctrlchannel_router.register(r'ctrlchannelparams',CtrlChannelParamViewSet, base_name='ctrlchannelparams' )

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(scenario_router.urls)),
    url(r'^', include(collection_router.urls)),
    url(r'^', include(linkctrlchannel_router.urls)),
]