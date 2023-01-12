#!/usr/bin/python3
"""script exports to-do list info for a given employee ID to JSON format."""

import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    res = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()

    for x in res:
        x.pop('userId')
        x.pop('id')
        x['username'] = user['username']
        x['task'] = x['title']
        x.pop('title')
    res = {user['id']: res}
    fname = str(user['id']) + '.json'
    with open(fname, 'w') as f:
        json.dump(res, f)
