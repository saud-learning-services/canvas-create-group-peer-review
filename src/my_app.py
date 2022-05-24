import random
import pandas as pd
from canvasapi import Canvas
import canvas_create_peer_reviews
import helpers
from helpers import _matches_dict_key_val

# DASH
from jupyter_dash import JupyterDash
from dash import dcc, html, Input, Output
from dash.dependencies import Input, Output

KEY = canvas_create_peer_reviews.API_KEY
URL = canvas_create_peer_reviews.API_URL
COURSEID = 10456
canvas = helpers.create_instance(URL, KEY)
course = canvas.get_course(COURSEID)
assignments = course.get_assignments()
group_categories = course.get_group_categories()

def my_app():

    assignments_list = [{'label': i.name, 'value': i.id} for i in assignments]
    group_categories_list = [{'label': i.name, 'value': i.id} for i in group_categories]

    def drop_down_div(list_of_dicts, dropdown_id, div_id):
        first_value = list_of_dicts[0].get('value')
        
        html_div = html.Div([
            dcc.Dropdown(options=list_of_dicts, value=first_value, id=dropdown_id),
            html.Div(id=div_id)
        ])
        
        return(html_div)

    def drop_down_div(list_of_dicts, dropdown_id, div_id):
        first_value = list_of_dicts[0].get('value')
        
        html_div = html.Div([
            dcc.Dropdown(options=list_of_dicts, value=first_value, id=dropdown_id),
            html.Div(id=div_id)
        ])
        
        return(html_div)

    app = JupyterDash(__name__)

    app.layout = html.Div(children=[
        html.H1(children=f"{course.name}"),
        drop_down_div(assignments_list, 'assignments-dropdown', 'dd-output-container'),
        html.Br(),
        drop_down_div(group_categories_list, 'group-categories-dropdown', 'dd-output-container2'),
        html.Br(),
        html.Div(id='all-output')
    ])

    @app.callback(
        Output('all-output', 'children'),
        Input('assignments-dropdown', 'value'),
        Input('group-categories-dropdown', 'value')
    )

    def update_output(assignmentval, groupcategoriesval):
        
        assignment_name = [d for d in assignments_list if _matches_dict_key_val(d, "value", assignmentval)][0].get('label')
        groupcategories_name = [d for d in group_categories_list if _matches_dict_key_val(d, "value", groupcategoriesval)][0].get('label')
                
        
        return html.Div(children=[html.H2(f'You have selected:'),
                                html.Div(f'Assignment: {assignment_name} ({assignmentval})'), html.Br(),
                                html.Div(f'Course Group:  {groupcategories_name} ({groupcategoriesval})')])

    app.run_server(mode='inline')