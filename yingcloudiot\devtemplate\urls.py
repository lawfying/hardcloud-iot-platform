from django.urls import include, url

from rest_framework_nested import routers
from .views import DevTemplateViewSet,TemplateTagsViewSet,TplDataChannelViewSet,TplDataUnitViewSet,\
TplCtrlChannelViewSet,TplCtrlUnitViewSet

from django.conf import settings
router = routers.SimpleRouter()
router.register(r'devtemplates', DevTemplateViewSet,base_name='devtemplates')
#先创建一个路由实例，再注册一个url
#第一级URL

devtemplate_router = routers.NestedSimpleRouter(router, r'devtemplates', lookup='devtemplates')
devtemplate_router.register(r'templatetags',TemplateTagsViewSet, base_name='templatetags' )
devtemplate_router.register(r'tpldatachannels', TplDataChannelViewSet, base_name='tpldatachannels')
devtemplate_router.register(r'tplctrlchannels', TplCtrlChannelViewSet, base_name='tplctrlchannels')
#第二级URL


tpldatachannel_router = routers.NestedSimpleRouter(devtemplate_router,r'tpldatachannels',lookup='tpldatachannels')
tpldatachannel_router.register(r'tpldataunits',TplDataUnitViewSet,base_name='tpldataunits')
#第三级URL

tplctrlchannel_router = routers.NestedSimpleRouter(devtemplate_router,r'tplctrlchannels',lookup='tplctrlchannels')
tplctrlchannel_router.register(r'tplctrlunits',TplCtrlUnitViewSet,base_name='tplctrlunits')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(devtemplate_router.urls)),
    url(r'^', include(tpldatachannel_router.urls)),
    url(r'^', include(tplctrlchannel_router.urls)),
]