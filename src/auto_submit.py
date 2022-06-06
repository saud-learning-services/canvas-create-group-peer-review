import random
import pandas as pd
from canvasapi import Canvas
import helpers
from helpers import _return_single_dict_match, _simplify_group_dicts, _create_custom_group_html
import json
import os
from dotenv import load_dotenv


load_dotenv() 

URL = os.getenv('API_INSTANCE')
KEY = os.getenv('API_TOKEN')
COURSE_ID = os.getenv('COURSE_ID')
GRAPH_URL = f"{URL}/api/graphql"

# incomplete - need to add assignment id
#ASSIGNMENT_ID = {ENTER ASSIGNMENT ID}

canvas = helpers.create_instance(URL, KEY)

course = canvas.get_course(COURSE_ID)
assignment = course.get_assignment(ASSIGNMENT_ID)
submissions = assignment.get_submissions()

for i in submissions:

    try:
        submission_dict = i.__dict__
        assignment_id = submission_dict.get("assignment_id")
        user_id = submission_dict.get("user_id")
        user_name = canvas.get_user(user_id).__dict__.get("name")
        submission_type = "online_text_entry"

        newDict = {"assignment_id": assignment_id,
        "user_id": user_id,
        "user_name": user_name,
        "submission_type": submission_type,
        "submission_body": f"Assignment Auto Submitted for: {user_name} ({user_id})."
        }
        
        print(newDict)

    except Exception as err:
        print(submission_dict, err)