# coding: utf-8

from django.urls import path

from rest_framework import routers
from .views import UserViewSet, MattViewSet, Log_dataViewSet
from . import views
from .views import plotlytestviews, log_graph

app_name='matt_log'

urlpatterns = [
    path('', plotlytestviews, name="plotlytest"),
    path('plotlytest/', plotlytestviews, name = 'plotlytest'),
    path('log_graph/', log_graph, name = 'Log_graph'),
]


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Matts', MattViewSet)
router.register(r'Log_datas', Log_dataViewSet)

