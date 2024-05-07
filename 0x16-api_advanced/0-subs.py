#!/usr/bin/python3
"""Import required module/lib"""
import requests


def number_of_subscribers(subreddit):
    """queries Reddit API and returns the number of subscribers"""
    if not subreddit:
        return 0
    else:
        r = requests.get('https://www.reddit.com/dev/api#GET_api_v1_me')
        return str(r)
