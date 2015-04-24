#!/usr/bin/python

import praw

from login_info import *

# naming bot to comply with Reddit API
user_agent = user_agent

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("mst3k")

for submission in subreddit.get_hot(limit = 10):
	print "Title: ", submission.title
	print "Text: ", submission.selftext
	print "Score: ", submission.score
	print " ----------------------- "