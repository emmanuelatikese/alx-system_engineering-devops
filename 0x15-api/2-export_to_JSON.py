#!/usr/bin/python3
'''This is all about getting json(extension)'''

if __name__ == "__main__":
    import json
    import requests
    from sys import argv
    if int(argv[1]):
        todos = 'https://jsonplaceholder.typicode.com/todos/?userId='
        name = 'https://jsonplaceholder.typicode.com/users/?id='
        req_title = requests.get(todos + argv[1])
        req_name = requests.get(name + argv[1])

        rt = req_title.json()
        name = req_name.json()[0].get('username')
        dt, lr = {}, {}
        k = "{}".format(argv[1])
        dt[k] = []

        for x in rt:
            lr['task'] = x.get('title')
            lr['completed'] = x.get('completed')
            lr['username'] = name
            dt[k].append(lr)
            lr = {}
        jsf = "{}.json".format(k)
        with open(jsf, "w") as jf:
            json.dump(dt, jf)
