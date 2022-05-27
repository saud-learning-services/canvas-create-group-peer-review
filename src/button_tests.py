import random
import pandas as pd
from canvasapi import Canvas
import helpers
from helpers import _return_single_dict_match, _simplify_group_dicts, _create_custom_group_html
from assign_peer_review_by_group import assign_peer_review_by_group
import json
from initial_request import get_initial_info
import os
from dotenv import load_dotenv

# DASH
from jupyter_dash import JupyterDash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

load_dotenv() 


def my_app():


    app = JupyterDash(__name__)

    app.layout = html.Div([
        html.H3('Select number of reviews to assign'),
        html.Div([
            html.Div(dcc.Input(id='input-on-submit', type='number'), style={'display': 'inline-block'}),
            html.Button('Assign Peer Reviews', id='submit-val', n_clicks=0, style={'display': 'inline-block'})
            ]),
        html.Div(id='container-button-basic',
                children='Enter a value and press submit')
    ])


    @app.callback(
        Output('container-button-basic', 'children'),
        Input('submit-val', 'n_clicks'),
        State('input-on-submit', 'value')
    )
    def update_output(n_clicks, value):
        return 'The input value was {} and the button has been clicked {} times'.format(
            value,
            n_clicks
        )


    app.run_server(mode='inline')