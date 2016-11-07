from django.conf.urls import include, url
from django.views.generic import TemplateView


# 首页配置
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="website/index.html") , name='index'),
    url(r'^about/$', TemplateView.as_view(template_name="website/about.html") , name='about'),
]