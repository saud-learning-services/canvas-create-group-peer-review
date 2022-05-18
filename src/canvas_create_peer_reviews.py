from helpers import create_instance, _get_course
from random_review_assignment import create_n_iterations
import os
from dotenv import load_dotenv

load_dotenv() 

API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')
COURSE_ID = 10456

if __name__ == "__main__":
    canvas = create_instance(API_URL, API_KEY)
    course = _get_course(canvas, COURSE_ID)