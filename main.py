__author__ = 'oddone'

import praw

reddit = praw.Reddit(user_agent='Path of Exile unique item helper')
subreddit = reddit.get_subreddit('pathofexile')

posts = subreddit.get_top_from_day()

for post in posts:
    for comment in post.comments:
        text = comment.body
