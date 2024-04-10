#!/usr/bin/python3
'''This is about listing titles'''
import requests

def top_ten(subreddit):
''' This is about listing '''
    header = {"User-Agent": "Chrome/120.0.0.0"}
    url = "https://reddit.com/r/{}/hot".format(subreddit)
    req = requests.get(url, params={'limit':10}, headers=header)
    if req.status_code == 200:
        try:
            dt = req.json()
            dt.get('data').get('children')
            title = dt.get('data').get('title')
            for x in data:
                print(x)
        except Exception:
            print("None")
