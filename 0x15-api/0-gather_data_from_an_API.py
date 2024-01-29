#!/usr/bin/python3
'''This is all about getting'''

if __name__ == "__main__":
    import requests
    from sys import argv
    if int(argv[1]):
        todos = 'https://jsonplaceholder.typicode.com/todos/?userId='
        name = 'https://jsonplaceholder.typicode.com/users/?id='
        req_title = requests.get(todos + argv[1])
        req_name = requests.get(name + argv[1])
        comp = [a for a in req_title.json() if a.get('completed') is True]
        lef = len(comp)
        tol = len(req_title.json())
        print('Employee {} is done with tasks({}/{}):'
              .format(req_name.json()[0].get('name'), lef, tol))
        [print('\t{}'.format(x.get('title'))) for x in comp]
