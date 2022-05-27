import random
import pandas as pd
from canvasapi import Canvas
import helpers
from helpers import _return_single_dict_match, _simplify_group_dicts, _create_custom_group_html
import json
from initial_request import get_initial_info
import os
from dotenv import load_dotenv

# DASH
from jupyter_dash import JupyterDash
from dash import dcc, html, Input, Output
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

load_dotenv() 

URL = os.getenv('API_INSTANCE')
KEY = os.getenv('API_TOKEN')
COURSE_ID = os.getenv('COURSE_ID')
GRAPH_URL = f"{URL}/api/graphql"

canvas = helpers.create_instance(URL, KEY)

course, assignments, group_sets, users = get_initial_info(GRAPH_URL, COURSE_ID, KEY)

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

        assignment_name = _return_single_dict_match(assignments_list, "value", assignmentval).get('label')
        groupcategories_name = _return_single_dict_match(group_sets_list, "value", groupcategoriesval).get('label')


        # Matching and cleaning up groups
        matched_group_category = _return_single_dict_match(group_sets, "_id", groupcategoriesval) 
        simple_groups_list = _simplify_group_dicts(matched_group_category)
        group_children_html = _create_custom_group_html(simple_groups_list)
    
        # matching and cleaning up assignments 
        matched_assignment = _return_single_dict_match(assignments, "_id", assignmentval) 
        matched_assignment_html = f'Set for Peer Reviews: {matched_assignment.get("peerReviews").get("enabled")}'

        return html.Div(children=[html.H2(f'You have selected:'),
                                html.H3(f'Assignment: {assignment_name} ({assignmentval})'), 
                                html.Div(matched_assignment_html), html.Br(),
                                html.H3(f'Course Group:  {groupcategories_name} ({groupcategoriesval})'),
                                html.Div(children = group_children_html)
                                ])
                               


    app.run_server(mode='inline')