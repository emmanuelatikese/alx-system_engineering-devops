#!/usr/bin/python3
'''This is a merely a commit about api'''
import requests

def number_of_subscribers(subreddit):
    header = {"User-agent": "Chrome/120.0.0.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url)
    if req.status_code == 200:
        try:
            scrap = req.json()
            num = scrap["data"]["subscribers"]
            return (num)
        except Exception as e:
            return (0)
