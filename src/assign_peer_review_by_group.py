from helpers import _return_single_dict_match, _matches_dict_key_val_list
from create_n_iterations import create_n_iterations


def _delete_submissions_peer_reviews(submissions):
    for i in submissions:

        submission_pr = i.get_submission_peer_reviews()

        for j in submission_pr:

            delete_reviewer = j.__dict__.get("assessor_id")
            i.delete_submission_peer_review(delete_reviewer)
            
    print(f"Deleted subset of peer reviews")

def _delete_all_assignment_peer_reviews(assignment):
    submissions = assignment.get_submissions()

    for i in submissions:

        submission_pr = i.get_submission_peer_reviews()

        for j in submission_pr:

            delete_reviewer = j.__dict__.get("assessor_id")
            i.delete_submission_peer_review(delete_reviewer)
            
    print(f"Deleted all peer reviews for {assignment.name}")

def _assign_user_submission_reviews(submission, reviewers):
    # assign new reviews
    #submission = assignment.get_submission(reviewee)
    
    submission = submission.get("submission")
    
    for i in reviewers:
        submission.create_submission_peer_review(i)
        
def _get_submission_status_per_user(assignment):
    submissions = assignment.get_submissions()
    
    submission_details = []
    
    for i in submissions:
        new_dict = {"user_id": i.user_id,
        "submission_id": i.id,
        "submission_missing": i.missing,
        "submission": i}
        
        submission_details.append(new_dict)
        
    return(submission_details)

def assign_peer_review_by_group(assignment, simple_groups_list, n_reviews):
    
    # get all submissions
    try:
        submission_details = _get_submission_status_per_user(assignment)
        print(f"Accessed submissions for {assignment.name}")
    except Exception as err:
        print(f"Error getting submission details: {err}")

    #try:
    #    _delete_all_assignment_peer_reviews(assignment)
    #
    #except Exception as err:
    #    print(f"Error in deleting current reviews: {err}")

    
    for i in simple_groups_list: 
        # uses canvas submission so need user_id to be int
        
        try:
            print(f"Accessing submissions for group: {i.get('group_name')}")
            group_users = [int(j.get("canvas_id")) for j in i.get("members")]
            submission_by_group = [j for j in submission_details if _matches_dict_key_val_list(j, "user_id", group_users)]
        
        except Exception as err:
            print(f"Error in group {i.get('group_name')}: {err}")
            
        #complete_submissions = [k for k in submission_by_group if _matches_dict_key_val(k, "submission_missing": False)]
        # what if NO submission(?) I think this will assign regardless
        list_dict, user_review_dict = create_n_iterations(group_users, n_reviews)

        for k in user_review_dict:
            reviewee = list(k.keys())[0]
            reviewers = list(k.values())[0]

            print(f"{reviewee} will be reviewed by: {reviewers}")

            submission = _return_single_dict_match(submission_by_group, "user_id", reviewee)
            
            try:
                _assign_user_submission_reviews(submission, reviewers)
            except Exception as err:
                print(f"Error in assigning reviews: {err}")