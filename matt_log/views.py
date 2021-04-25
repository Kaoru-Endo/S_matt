from django.shortcuts import render

# Create your views here.

import datetime
import django_filters
from rest_framework import viewsets, filters

from .models import User, Matt, Log_data
from .serializer import UserSerializer, MattSerializer, Log_dataSerializer

from django.views.generic import TemplateView
import plotly.graph_objects as go
from .plotgraph import log_graph_plot


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MattViewSet(viewsets.ModelViewSet):
    queryset = Matt.objects.all()
    serializer_class = MattSerializer

class Log_dataViewSet(viewsets.ModelViewSet):
    queryset = Log_data.objects.all()
    serializer_class = Log_dataSerializer

def plot_graph(num):
    matt_num = num
    Auto = ""

    log_data_list = Log_data.objects.all().filter(s_matt_id = matt_num)
    a=[]
    b=[]
    for data in log_data_list:
        a.append(data.created_at + datetime.timedelta(hours=9))
        b.append(data.quantity)

    matt = Matt.objects.values('name').get(matt_id = matt_num)
    print(type(matt))
    print(matt)
    print(matt['name'])

    plot = log_graph_plot(a,b,matt['name'])

    return plot



def log_graph(request):

    if request.method == 'POST':
        matt_num = request.POST['matt_id']
        Auto = request.POST['Auto']
    else:
        matt_num = 1
        Auto = ""

#
#    log_data_list = Log_data.objects.all().filter(s_matt_id = matt_num)
#    a=[]
#    b=[]
#    for data in log_data_list:
#        a.append(data.created_at + datetime.timedelta(hours=9))
#        b.append(data.quantity)
#
#    matt = Matt.objects.values('name').get(matt_id = matt_num)
#    print(type(matt))
#    print(matt)
#    print(matt['name'])

    matt_list = Matt.objects.all()
    print(matt_list)
    print(Matt)

    n=0
#    plot=list(range(4))
    plot=[]
    for s_matt_id in matt_list:
        print(s_matt_id)
        plot += [plot_graph(n+1)]
        n = n + 1

    return render(request, 'matt_log/plotlytest.html', {'plot1': plot[0], 'plot2': plot[1], 'plot3': plot[2], 'plot4': plot[3], 'Auto':Auto,})

