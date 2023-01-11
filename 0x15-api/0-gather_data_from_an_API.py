#!/usr/bin/python3
"""this script returns to-do list information for a given employee ID."""
import requests, sys


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com'

    name = requests.get(url + '/users/{}'.format(sys.argv[1])).json()['name']

    res = requests.get(url + '/todos', params={'userId': sys.argv[1]}).json()

    cpd_tasks = [x for x in res if x['completed'] is True]
    print('Employee {} is done with tasks({}/{}):'.format(name, len(cpd_tasks), len(res)))
    for i in cpd_tasks:
        print('\t' + i['title'])

