import numpy as np
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.offline import plot
import pandas as pd

from S_matt.settings import BASE_DIR
import os

def log_graph_plot(a,b,name):

    data_x = a
    data_y = b

#    df_positive = pd.read_csv(os.path.join(BASE_DIR, 'matt_log/Stock.csv'))
    fig = go.Figure()
    #fig.add_trace(go.Scatter(x=df_positive['日付'], y=df_positive['在庫数'],
    fig.add_trace(go.Scatter(x=data_x, y=data_y,
                             mode='lines+markers',
                             name='positive'))

    fig.layout.update({'title': '物品名 ： '+ name})
    fig.layout.xaxis.update({'title': '日付'})
    fig.layout.yaxis.update({'title': '在庫数'})
    fig.layout.update({'margin': {'r':10, 'l':10, 't':40, 'b':10}})
    fig.layout.update({'height': 400})
    fig.update_layout(title_text='物品名 ： '+name)
    plot_fig = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_fig
