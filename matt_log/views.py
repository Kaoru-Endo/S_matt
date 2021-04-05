from django.shortcuts import render

# Create your views here.

import datetime
import django_filters
from rest_framework import viewsets, filters

from .models import User, Matt, Log_data
from .serializer import UserSerializer, MattSerializer, Log_dataSerializer

from django.views.generic import TemplateView
import plotly.graph_objects as go
from .plotgraph import plotlytest_graph, plot_graph


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MattViewSet(viewsets.ModelViewSet):
    queryset = Matt.objects.all()
    serializer_class = MattSerializer

class Log_dataViewSet(viewsets.ModelViewSet):
    queryset = Log_data.objects.all()
    serializer_class = Log_dataSerializer


def plotlytestviews(request):


    log_data_list = Log_data.objects.all().filter(s_matt_id = 1)

    a=[]
    b=[]

    print("+++++++++++++")
    for data in log_data_list:
        a.append(data.created_at + datetime.timedelta(hours=9))
        b.append(data.quantity)
        print(a, b)
    print("=============")


    plot = plotlytest_graph(a,b)

    return render(request, 'matt_log/plotlytest.html', {'plot': plot})

def log_graph(request):
    log_data_list = Log_data.objects.all()

    plot = plot_graph(log_data_list)

    return render(request, 'matt_log/plotlytest.html', {'plot': plot})


