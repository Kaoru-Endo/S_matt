import numpy as np
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.offline import plot
import pandas as pd

from S_matt.settings import BASE_DIR
import os

def plotlytest_graph(a,b):

    data_x = a
    data_y = b

#    df_positive = pd.read_csv(os.path.join(BASE_DIR, 'matt_log/Stock.csv'))
    fig = go.Figure()
    #fig.add_trace(go.Scatter(x=df_positive['日付'], y=df_positive['在庫数'],
    fig.add_trace(go.Scatter(x=data_x, y=data_y,
                             mode='lines',
                             name='positive'))

    fig.layout.update({'title': '物品A　在庫数推移'})
    fig.layout.xaxis.update({'title': '日付'})
    fig.layout.yaxis.update({'title': '在庫数'})
    fig.update_layout(title_text='物品A　在庫数推移')
    plot_fig = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_fig

def plot_graph(object_list):

    return