from canvasapi import Canvas
import util
import sys
import pandas as pd
import ipywidgets as widgets
from IPython.display import display

def _matches_dict_key_val(dic, key, matches_val):
    '''Returns the dictionary if the provided key matches the match_val
    
    parameters:
        dic (dict)
        key (string): the key string in the dict to find
        matches_val (str|int): they str or int to try to find in the key

    returns:
        boolean
    '''
    # for use in list , example:
    # [d for d in list if _matches_dict_id(d, "key", matches_val)]
    return(dic[f"{key}"] == matches_val)

def _return_single_dict_match(some_list, match_key, match_val):
            out = [d for d in some_list if _matches_dict_key_val(d, match_key, match_val)][0]
            return(out)

  
def _simplify_group_dicts(matched_group_category):
    some_list = []
    for i in matched_group_category.get("groupsConnection").get("nodes"):
        group_name = i.get('name')
        members = i.get('membersConnection').get('nodes')
        members_list = []

        for j in members:
            member = j.get("user")
            member_dict = {
                "name": member.get("name"),
                "canvas_id": member.get("_id"),
                "sis_id": member.get("sisId")
            }
            members_list.append(member_dict)

        new_dict = {
            "group_name": group_name,
            "members": members_list
        }

        some_list.append(new_dict)
    
    return(some_list)


def _create_custom_group_html(some_list):

    all_divs = []
    
    for i in some_list:
        
        new_div = html.Div(children= [
            html.H4(i.get('group_name')),
            html.Div(children = [
                html.P(f'{j.get("name")} ({j.get("canvas_id")})') for j in i.get('members')
            ])
        ])
        
        all_divs.append(new_div)
        
    return(all_divs)

def __create_dicts(paginated_list):
    '''Canvas objects are often paginated lists, return as a list of dictionaries'''
    list_of_dicts = [i.__dict__ for i in paginated_list]
    return(list_of_dicts)


def create_instance(API_URL, API_KEY):
    try:
        canvas = Canvas(API_URL, API_KEY)
        util.print_success("Token Valid: {}".format(str(canvas.get_user('self'))))
        return(canvas)
    except Exception as e:
        util.print_error("\nInvalid Token: {}\n{}".format(API_KEY, str(e)))
        sys.exit(1)
        #raise

def _get_course(canvas_obj, course_id):
    '''
    Get Canvas course using canvas object from canvasapi
    Parameters:
        course (Canvas): canvasapi instance
        course_id (int): Canvas course ID
    Returns:
        canvasapi.course.Course object
    '''
    try:
        course = canvas_obj.get_course(course_id)
        util.print_success(f'Entered id: {course_id}, Course: {course.name}.')
    except Exception:
        util.shut_down(f'ERROR: Could not find course [ID: {course_id}]. Please check course id.')

    return course

def get_group_data(course):
    # get groups from course
    try:
        groups = course.get_groups(per_page=50)

        try:
            groups[0]
        except IndexError:
            util.shut_down(f'No groups found in the course {course.name}.')

        all_groups = []

        for group in groups:
            
            users_list = group.get_users()
            
            for user in users_list:
                group_dict = {}
                group_dict['group_id'] = group.id
                group_dict['group_name'] = group.name
                #group_dict['group_created_at'] = group.created_at
                group_dict['course_name'] = course.name
                group_dict['course_id'] = course.id
                #print(group, user)
                group_dict['user_id']= user.id
                group_dict['user_name']= user.name
            
                all_groups.append(group_dict)

            # membership_list = group.get_memberships()
            # for member in membership_list:
            #     group_dict['moderator'] = member.moderator
            #     #group_dict['workflow_state'] = member.workflow_state
            #     #group_dict['membership_id'] = member.id
            
        return(pd.DataFrame(all_groups))

    except Exception as e:
        util.shut_down("Something went wrong: {}".format(str(e)))