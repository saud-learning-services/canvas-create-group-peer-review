# Canvas Create Group Peer Review
> IN DEVELOPMENT!
> - "Works" - but does not handle errors well! Use at your discretion
> - Sharing in development phase in case useful to others. 

The jupyter notebook **dash-app.ipynb** allows the user to select an assignment, select canvas group sets and assigns X peer reviews. 

## Important Notes

1. You need to have created a .env file -> add your url, token, and course_id
2. This process allows you to select an assignment and a group set from your course
3. You can then N peer reviews that will be applied within the groups in the selected group set
> Note: you must set N to at least 1 less than members in the groups
4. ⚠️ Running this will **delete ALL current peer reviews** for the assignment (this cannot be undone)
5. The peer review assignment is random, so when you run will be different each time

▶️ When you are ready select Kernel -> Restart & Run All.
▶️ If you make any changes you need to Restart & Run All to refresh the data

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

#### Every Time

1. Update your .env file

1. Run:
   1. navigate to your directory `$ cd YOUR_PATH/canvas-create-group-peer-reviews`
   1. activate the environment (see step 3 on first run) `$ conda activate canvas-create-group-peer-review`
   1. in terminal launch jupyter notebook `$ jupyter notebook dash-app.ipynb`
   1. follow prompts in jupyter notebook 

---
_authors: @alisonmyers_