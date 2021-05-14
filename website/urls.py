#  hello/urls.py
from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('contact', views.contact_page_view, name='contact'),
    path('info', views.info_page_view, name='info'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]
