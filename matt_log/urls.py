# coding: utf-8

from django.urls import path

from rest_framework import routers
from .views import UserViewSet, MattViewSet, Log_dataViewSet
from . import views
from .views import log_graph

app_name='matt_log'

urlpatterns = [
    path('', log_graph, name="log_graph"),
    path('log_graph/', log_graph, name = 'log_graph'),
]


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Matts', MattViewSet)
router.register(r'Log_datas', Log_dataViewSet)

