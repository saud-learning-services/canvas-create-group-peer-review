import requests
import json
import os

# uses GRAPH QL

def _get_query_by_course(url, query, course_id, KEY):
    
    r = requests.post(url, json={'query': query, "variables": {"id": f"{course_id}"}}, headers={'Authorization': f'Bearer {KEY}'})
    if r.status_code == 200:
        return(r.json())
    else:
        print(f"Error: {r.json()}")
        
def get_initial_info(url, course_id, KEY):
    
    query = """query($id: ID) {
      course(id: $id) {
        id
        _id
        courseCode
        name
        usersConnection(filter: {enrollmentStates: active}) {
          nodes {
            id
            sisId
            sortableName
            _id
            name
            enrollments(courseId: $id) {
                type
            }
          }
        }
        assignmentsConnection {
          nodes {
            id
            _id
            name
            peerReviews {
              enabled
            }
          }
        }
        groupSetsConnection {
          nodes {
            name
            _id
            groupsConnection {
              nodes {
                _id
                name
                membersCount
                membersConnection {
                  nodes {
                    user {
                      _id
                      name
                      sisId
                    }
                  }
                }
              }
            }
          }
        }
      }
    }

    """

    try:
        
        all_json = _get_query_by_course(url, query, course_id, KEY)
        assignments = all_json['data']['course']['assignmentsConnection']
        group_sets = all_json['data']['course']['groupSetsConnection']['nodes']
        course = { your_key: all_json['data']['course'][your_key] for your_key in ['_id', 'id', 'courseCode', 'name'] }
        users = all_json['data']['course']['usersConnection']['nodes']
        return(course, assignments, group_sets, users)
        
    except Exception as err:
        print(f'Error: {err}')


    