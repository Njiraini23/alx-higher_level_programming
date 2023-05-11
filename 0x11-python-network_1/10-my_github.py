#!/usr/bin/python3
"""Takes the Github username and password and uses
the Github API to display my id
"""
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    response = get(url, auth=HTTPBasicAuth(username, password))
    obj = response.json()
    print(obj.get('id'))
