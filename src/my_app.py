import random
import pandas as pd
from canvasapi import Canvas
import canvas_create_peer_reviews
import helpers
from helpers import _matches_dict_key_val
import json

from initial_request import get_initial_info

# DASH
from jupyter_dash import JupyterDash
from dash import dcc, html, Input, Output
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

KEY = canvas_create_peer_reviews.API_KEY
URL = canvas_create_peer_reviews.API_URL
GRAPH_URL = f"{URL}/api/graphql"
COURSEID = canvas_create_peer_reviews.COURSE_ID

canvas = helpers.create_instance(URL, KEY)

course, assignments, group_sets, users = get_initial_info(GRAPH_URL, COURSEID, KEY)

def my_app():

    assignments_list = [{'label': i.get('name'), 'value': i.get('_id')} for i in assignments]
    group_sets_list = [{'label': i.get('name'), 'value': i.get('_id')} for i in group_sets]

    def drop_down_div(list_of_dicts, dropdown_id, div_id):
        first_value = list_of_dicts[0].get('value')
        
        html_div = html.Div([
            dcc.Dropdown(options=list_of_dicts, value=first_value, id=dropdown_id),
            html.Div(id=div_id)
        ])
        
        return(html_div)

    app = JupyterDash(__name__)

    app.layout = html.Div(children=[
        html.H1(children=f"{course.get('name')}"),

        html.Div(children=[
            drop_down_div(assignments_list, 'assignments-dropdown', 'dd-output-container'),
            html.Br(),
            drop_down_div(group_sets_list, 'group-categories-dropdown', 'dd-output-container2'),
            html.Br(),
            html.Div(id='all-output'),
            html.Br()]),

        html.Div(id="body-div", 
            children=[])

    ])

    @app.callback(
        Output('all-output', 'children'),
        Input('assignments-dropdown', 'value'),
        Input('group-categories-dropdown', 'value')
    )

    def update_output(assignmentval, groupcategoriesval):

        def _return_single_dict_match(some_list, match_key, match_val):
            out = [d for d in some_list if _matches_dict_key_val(d, match_key, match_val)][0]
            return(out)

        assignment_name = _return_single_dict_match(assignments_list, "value", assignmentval).get('label')
        groupcategories_name = _return_single_dict_match(group_sets_list, "value", groupcategoriesval).get('label')

        matched_group_category = _return_single_dict_match(group_sets, "_id", groupcategoriesval) 
        matched_assignment = _return_single_dict_match(assignments, "_id", assignmentval) 

        return html.Div(children=[html.H2(f'You have selected:'),
                                html.H3(f'Assignment: {assignment_name} ({assignmentval})'), 
                                html.Div(f'{matched_assignment}'), html.Br(),
                                html.H3(f'Course Group:  {groupcategories_name} ({groupcategoriesval})'),
                                html.Div(f'{matched_group_category}')
                                ])
                               

    app.run_server(mode='inline')