# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 18:44:06 2016

@author: Isidora
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^studenti$', views.ViewStudenti.as_view(), name='studenti'),
    url(r'^predmeti$', views.ViewPredmeti.as_view(), name='predmeti'),
    url(r'^detailStudent(?P<pk>[0-9]+)/$', views.DetailViewStudent.as_view(), name='detailStudent'),
    url(r'^detailPredmet(?P<pk>[0-9]+)/$', views.DetailViewPredmet.as_view(), name='detailPredmet'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResutlsView.as_view(), name='rezultati'),
   # url(r'^(?P<pitanje_id>[0-9]+)/oceni/$', views.oceni, name='oceni')
]