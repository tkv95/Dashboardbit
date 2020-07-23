# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:05:26 2020

@author: Admin
"""

import dash
import dash_bootstrap_components as dbc
app = dash.Dash(__name__,external_stylesheets =[dbc.themes.BOOTSTRAP])
server = app.server
app.config.suppress_callback_exceptions =True