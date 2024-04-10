#!/usr/bin/python3
'''This is recurse'''
import requests

def recurse(subreddit, hot_list=[]):
    '''This is a recurse'''
    after=None
    hot_lt = [] if hot_list is None else hot_list
    url = "https://ww.reddit.com/r/{}/hot.json?limit=100".format(subreddit}
    if after:
        url += "after={}".format(after)
    header = {"User-Agent": "Chrome/120.0.0.0"}
    res = requests.get(url, headers=header}
    if res.status_code == 200:
        try:
            dt = res.json()
            pt = dt.get('data').get('children')
        if not pt:
            return pt
        [hot_lt.append(pt['data']['title'] for x in pt]
        after = dt['data']['after']
        return recurse(subreddit, hot_lt, after)
        except Exception:
            return None
