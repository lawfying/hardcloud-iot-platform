"""yingcloudiot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
#from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, RedirectView
from rest_framework_swagger.views import get_swagger_view

from django.conf import settings
admin.site.site_header = "YingCloud IoT 后台管理"
admin.site.site_title = "YingCloud IoT Admin Portal"
admin.site.index_title = "Welcome to YingCloud IoT Portal"

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

#201911sst
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
#201911sst

schema_view_redoc = get_schema_view(
    openapi.Info(
        title="IOT API接口文档平台",    # 必传
        default_version='v1',   # 必传
        description="这是接口文档",
        terms_of_service="https://www.yingcloud.com",
        contact=openapi.Contact(email="yingcloudiot@163.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),   # 权限类
)

schema_view = get_swagger_view(title='API')

urlpatterns = [
    path('admin/', admin.site.urls),
    #######
    path(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    path(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
    path(r'^email-verification/$',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),
    path(r'^login/$', TemplateView.as_view(template_name="login.html"),
        name='login'),
    path(r'^logout/$', TemplateView.as_view(template_name="logout.html"),
        name='logout'),
    path(r'^password-reset/$',
        TemplateView.as_view(template_name="password_reset.html"),
        name='password-reset'),
    path(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password-reset-confirm'),

    path(r'^user-details/$',
        TemplateView.as_view(template_name="user_details.html"),
        name='user-details'),
    path(r'^password-change/$',
        TemplateView.as_view(template_name="password_change.html"),
        name='password-change'),


    # this url is used to generate email content
    path(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),

    #########
    path(r'^redoc/', schema_view_redoc.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #url(r'^apis/', schema_view,name='restapi'),  
    path(r'^accounts/', include('allauth.urls')),
    path(r'^rest-auth/', include('accounts.urls')),
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
    path(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
    path(r'^token-api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'^token-api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'^token-api/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
    path(r'^rest-auth/', include('rest_auth.urls')),
    path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    path(r'^', include('devtemplate.urls')),
    path(r'^', include('device.urls')),
    path(r'^', include('scenario.urls')),
    path(r'^trigger/', include('trigger.urls')),
    path(r'^iotsubdev/', include('iothub.urls')),
    path(r'^dashboard/', include('dashboard.urls')),
    path(r'^docs/$', get_swagger_view(title='API Docs'), name='api_docs')
]

#static
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )