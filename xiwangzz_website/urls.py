from django.conf.urls import include, url
from django.views.generic import TemplateView,RedirectView
from xiwangzz import settings

# 首页配置
urlpatterns = [
    url(r'^$' , TemplateView.as_view(template_name="website/index.html") , name='index'),
    url(r'^about/$' , TemplateView.as_view(template_name="website/about.html") , name='about'),
    url(r'^magzine/$' , TemplateView.as_view(template_name="website/magzine.html") , name='magzine'),
    url(r'^contact/$' , TemplateView.as_view(template_name="website/contact.html") , name='contact'),

    url(r'^favicon\.ico$' , RedirectView.as_view(url=settings.STATIC_URL+'website/favicon.ico',permanent=True) , name='favicon'),
]