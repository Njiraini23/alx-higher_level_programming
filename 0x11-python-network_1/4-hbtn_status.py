#!/usr/bin/python3
"""
A script fetches https://intranet.hbtn.io/status.
Using the package requests
"""
from requests import get


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = get(url)
    contents = response.text
    string = 'Body response:\n\t- type: {}\n\t- content: {}'.format(
             type(contents), contents)
    print(string)
