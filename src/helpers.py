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

def __create_dicts(paginated_list):
    '''Canvas objects are often paginated lists, return as a list of dictionaries'''
    list_of_dicts = [i.__dict__ for i in paginated_list]
    return(list_of_dicts)



def create_group_category_dropdown(canvas, course):
    
    some_list = [(i.name, i.id) for i in course.get_group_categories()]
    
    w = widgets.Dropdown(
        options=some_list,
        description="Select value")
    
    global output
    
    output = widgets.Output()

    def on_change(change):
        global selected_val
        global group_category
        global groups

        if change['type'] == 'change' and change['name'] == 'value':
            output.clear_output()
                
            with output:
                selected_val = w.value        
                group_category = canvas.get_group_category(selected_val)
                groups = group_category.get_groups()
                
                for i in groups:
                    print(i.name)
                    members = i.get_memberships()
                    for j in members:
                        print(j)
                        
    w.observe(on_change)
    display(w)
    display(output)


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