# from django.conf.urls import url, include
from django.urls import path

from siteMenuPrincipal.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
