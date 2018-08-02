"""LxEnterprise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path, include
from apps.news import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  # 首页
                  path('', views.index, name='index'),
                  # 搜索
                  path('search', views.search, name='search'),
                  # 新闻
                  path('news/', include('apps.news.urls')),
                  # 后台
                  path('cms/', include('apps.cms.urls')),
                  # 登录
                  path('account/', include('apps.userauth.urls')),
                  # 课程
                  path('course/', include('apps.course.urls')),
                  # 付费
                  path('payinfo/', include('apps.payinfo.urls')),
                  # 验证码
                  path(r'captcha/', include('captcha.urls')),
                  # ueditor
                  path('ueditor/', include('apps.ueditor.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 配置debug_toolbar
if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
