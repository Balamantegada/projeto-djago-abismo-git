# from django.conf.urls import url, include
from django.urls import path

from siteMenuPrincipal.views import IndexView, CamadasViews

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('camadas/', CamadasViews.as_view(), name='camadas'),
]
