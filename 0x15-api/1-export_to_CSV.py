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
        name = req_name.json()[0].get('username')
        filename = "{}.csv".format(argv[1])
        with open(filename, 'w') as f:
            pass

        with open(filename, 'a') as r:
            for x in rt:
                uId = x.get("userId")
                com = x.get("completed")
                title = x.get("title")
                r.write('"{}","{}","{}","{}"\n'.format(uId, name, com, title))
