# Canvas Create Group Peer Review
> IN DEVELOPMENT!
> Questions? Ask Alison - alison.myers@sauder.ubc.ca
> - "Works" - but does not handle errors well! Use at your discretion
> - ⛔️ You cannot "undo" assignment of peer reviews! When you run the script it will delete any existing peer reviews even if there is an error (and no other peer reviews are assigned)

The jupyter notebook **dash-app.ipynb** allows the user to select an assignment, select canvas group sets and assigns X peer reviews.

## Important Notes
⚠️ Running this will **delete ALL current peer reviews** for the assignment (this cannot be undone)

The peer review assignment is random, so when you run will be different each time

The data for a course is pulled once, so you must Restart and Run All in Jupyter if any Canvas changes are made 
>   ▶️ If you make any changes you need to select Kernel -> Restart & Run All to refresh the data


## Input
- Canvas Instance _(instance of Canvas being used - ex. https://ubc.instructure.com)_
- Canvas API Token _(generate through Account => Settings)_
- Course ID _(last digits of URL when visiting course page)_
- Assignment Name _(the assignment to which group peer reviews will be assigned)_
- Group Set Name _(the name of the Group Set that contains the groups within which the peer reviews will be assigned)_
- N _(the number of peer reviews each group member should do)_


## Instructions

1. Create a .env file. Add your URL, token, and course id to the file.
```
API_TOKEN = ''
API_INSTANCE = 'https://ubc.instructure.com'
COURSE_ID = 
```
2. Choose the Assignment and the Group Set from two dropdown lists.
3. Enter the number of peer reviews you want to assign to each member.
   This number must be at least 1 less than the amount of members in the smallest group.

▶️ When you are ready select Kernel -> Restart & Run All.


## Output

On Canvas, the selected amount of peer reviews have been assigned within the chosen group set for the chosen assignment.

## Getting Started
### Sauder Operations

_Are you Sauder Operations Staff? Please go [here](https://github.com/saud-learning-services/instructions-and-other-templates/blob/main/docs/running-instructions.md) for detailed instructions to run in Jupyter. ("The Project", or "the-project" is "canvas-create-group-peer-review" or "Canvas Create Group Peer Review")._

### General (terminal instructions)
> Project uses **conda** to manage environment (See official **conda** documentation [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file))

#### First Time

1. Ensure you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed (Python 3.9 version)
2. Clone canvas-create-group-peer-review repository
3. Import environment (once): `$ conda env create -f environment.yml`
4. Create .env file and include:

```
API_TOKEN = ''
API_INSTANCE = 'https://ubc.instructure.com'
COURSE_ID = 
```
Your .env file should be in this project folder.

![image](https://user-images.githubusercontent.com/22600917/171711768-535fe292-2aef-4c32-8bc4-87788131a57a.png)

#### Every Time

1. Update your .env file

2. Run:
   1. navigate to your directory `$ cd YOUR_PATH/canvas-create-group-peer-reviews`
   2. activate the environment (see step 3 on first run) `$ conda activate canvas-create-group-peer-review`
   3. in terminal launch jupyter notebook `$ jupyter notebook dash-app.ipynb`
   4. follow prompts in jupyter notebook 

---
_authors: @alisonmyers_
