#!/usr/bin/python3
"""script exports to-do list information for a given employee ID to CSV format."""

import csv
import json
import requests
import sys

url = 'https://jsonplaceholder.typicode.com/'
user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()

res = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()

fname = str(user['id']) + '.csv'
with open(fname, 'x') as f:
    fil_e = csv.writer(f, quoting=csv.QUOTE_ALL)
    for row in res:
        entry = [
            row['userId'], user['username'], row['completed'], row['title']]
        fil_e.writerow(entry)
