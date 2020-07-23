# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 13:49:38 2020

@author: Admin
"""
import app
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import dash_table

import pandas as pd
import sqlite3

import plotly.graph_objs as go

conn= sqlite3.connect(r"C:/Users/Admin/Downloads/wine_data.sqlite")
c =conn.cursor()

df= pd.read_sql("select * from wine_data",conn)
df=df = df[['country', 'description', 'rating', 'price','province','title','variety','winery','color']]
df.head()

layout =html.Div([
    dcc.Tabs(id="tabs",value='tab-1',
             children=[
             dcc.Tab(label='Tab one',value='tab-1'),
             dcc.Tab(label='Tab two',value='tab-2'),
             ]),
    html.Div(id='tab-content')
    ])

if __name__ == "__main__":
    app.run_server(debug=True)