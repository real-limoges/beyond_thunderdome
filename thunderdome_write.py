import praw
import pdb
import re
import os
import time

from praw.errors import RateLimitExceeded
from requests.exceptions import HTTPError

from login_info import *

def sign_in():
	'''Opens praw reddit session and logs into Reddit
	   Returns the reddit session'''

	user_agent = agent_name
	r = praw.Reddit(user_agent = user_agent)

	r.login(REDDIT_USERNAME, REDDIT_PASSWORD)

	return r

def get_replied_to():
	'''If program has been run, it loads the log file of reponses.
	   Otherwise it returns and empty list'''

	if not os.path.isfile("replied_to.txt"):
		replied_to = []
		return replied_to

	with open("replied_to.txt", 'r') as f:
		replied_to = f.read()
		replied_to = replied_to.split('\n')
		replied_to = filter(None, replied_to)
		return replied_to

def check_reddit(r, replied_to):
	subreddit = r.get_subreddit('pythonforengineers')

	for submission in subreddit.get_hot(limit = 10):
		print submission.title

		if submission.id not in replied_to:
			if re.search("i love python", submission.title, re.IGNORECASE):
				try:
					submission.add_comment("Thunderbot Strikes Again!")
					print "Bot replied to: ", submission.title
				except RateLimitExceeded:
					print "you exceeded the rate"
				replied_to.append(submission.id)
	return replied_to

def write_file(replied_to):
	with open("replied_to.txt", 'a') as f:
		for post_id in replied_to:
			f.write(post_id + "\n")

def main():
	r = sign_in()
	replied_to = get_replied_to()

	while True:
		try:
			replied_to = check_reddit(r, replied_to)
		except HTTPError:
			continue
		time.sleep(60)

	write_file(replied_to)


main()