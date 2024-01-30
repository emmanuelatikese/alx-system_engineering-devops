#!/usr/bin/python3
'''This is all about getting json(extension)'''

if __name__ == "__main__":
    import json
    import requests

    todos = 'https://jsonplaceholder.typicode.com/todos/?userId='
    name = 'https://jsonplaceholder.typicode.com/users/?id='
    dt = {}
    for a in range(1, 11):
        lits, lr = [], {}
        k = str(a)
        req_title = requests.get(todos + k)
        req_name = requests.get(name + k)
        rt = req_title.json()
        print(rt)
        username = req_name.json()[0].get('username')
        for x in rt:
            lr['username'] = username
            lr['task'] = x.get('title')
            lr['completed'] = x.get('completed')
            lits.append(lr)
            lr = {}
        dt[k] = lits
    jsf = 'todo_all_employees.json'
    with open(jsf, "w") as jf:
        json.dump(dt, jf)
