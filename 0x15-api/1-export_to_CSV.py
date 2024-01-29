#!/usr/bin/python3
'''This is all about getting (extension)'''

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv
    if int(argv[1]):
        todos = 'https://jsonplaceholder.typicode.com/todos/?userId='
        name = 'https://jsonplaceholder.typicode.com/users/?id='
        req_title = requests.get(todos + argv[1])
        req_name = requests.get(name + argv[1])

        rt = req_title.json()
        i = 0
        while i < len(rt):
            rt[i]['username'] = req_name.json()[0].get('username')
            rt[i].pop('id')
            i += 1
        fi = ['userId', 'username', 'completed', 'title']
        with open('2.csv', 'w', newline='') as f:
            c = csv.DictWriter(f, fi)
            c.writeheader()
            c.writerows(rt)
