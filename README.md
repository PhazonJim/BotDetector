# BOTDETECTOR
A set of tools that allows the use of python plugins to easily process comment, submission, and modlog streams from PRAW (Python reddit API wrapper)

# Environment setup instructions
1. Ensure Python 3.10 or higher is installed
2. `cd` into project workspace
3. (Optional) to setup a local virtual environment you can run `python -m venv .venv`
    - On Windows in bash you can run: `.venv\Scripts\activate.bat`
    - On Mac OS and Linux you can run `source .venv/bin/activate`
4. run `pip install -r requirements.txt` to install dependencies

# Configuration
1. Rename config.example to config.yaml and set the following fields:
    - `client`: this is your reddit authentication data
    - `subreddit`: This supports multiple subreddits, you can use something like `mysubredditname` or `mysub+mysub2+othersub` to combine multiple. 
    - `comments_to_fetch`: this is how many comments you want to fetch from the API each time the script runs. The max value PRAW can return is 1000. Consider using a smaller number if you run this frequently.
    - `minimum_comment_size`: any comments with a character count less than this number are not checked. Useful for ignoring things like "yes" and "no" replies. 

# Usage
1. `cd` into project workspace
2. run `python main.py`

# Testing
TBD