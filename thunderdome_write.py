import praw
import pdb
import re
import os

from login_info import *

# Setup session
user_agent = user_agent
r = praw.Reddit(user_agent = user_agent)

print REDDIT_USERNAME, REDDIT_PASSWORD

# Login to Reddit
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)

# Check if code has been run
# If not, create an empty list to remember posts replied to
if not os.path.isfile("replied_to.txt"):
	replied_to = []

# Otherwise I've run the code before - open the file to remember this
else:
	with open("replied_to.txt", 'r') as f:
		replied_to = f.read()
		replied_to = replied_to.split('\n')
		replied_to = filter(None, replied_to)