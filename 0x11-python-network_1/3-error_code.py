#!usr/bin/python3
"""
Takes URL sends a request to the URL and displays
the body of response decoded in utf-8).
uses the packages urllib and sys
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as err:
        print('Error code: {}'.format(err.code))
