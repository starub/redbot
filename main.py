from pprint import pprint

import praw
import db

reddit = praw.Reddit(user_agent='Path of Exile unique item helper')
subreddit = reddit.get_subreddit('pathofexile')

posts = subreddit.get_top_from_day()

all_items = db.load()

for post in posts:
    for comment in post.comments:
        text = comment.body
        for item_categories in all_items:
            for items in item_categories:
                for item in items:
                    if item['name'] in text:
                        print('-------------------')
                        pprint(text)
                        pprint(item, indent=4)
                        print('-------------------')
