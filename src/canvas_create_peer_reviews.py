from helpers import create_instance, _get_course
from random_review_assignment import create_n_iterations
import os
from dotenv import load_dotenv

load_dotenv() 

API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')
COURSE_ID = os.getenv('COURSE_ID')

#TODO input n peer reviews

def get_group_sets(course):
    # given a course
    # get group sets
    # add user selector to select group set
    # get group number
    # returns group id
    return

def get_group_members(GROUP_ID):
    # given a group ID
    # get group users
    # https://canvas.ubc.ca/api/v1/group_categories/{GROUP_ID}/users
    return

def get_user_lists(group_members):
    # from returned group memberships
    # get a list of user ids
    # return a dictionary
    # {group_name: [userid, userid, userid]}
    return

def get_group_peer_reviews():
    # given a dict of groups (group_dict)
    # use the create_n_iterations function 
    return

if __name__ == "__main__":
    canvas = create_instance(API_URL, API_KEY)
    course = _get_course(canvas, COURSE_ID)

    #TODO - get all group sets
    group_id = get_group_sets(course)
    group_members = get_group_members(group_id)

    # 
    group_dict = get_user_lists(group_members)

    