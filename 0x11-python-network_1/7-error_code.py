#!/usr/bin/python3
"""
A script that takes URL,sends a request to URL and
displays body of response. print error code of HTTP
Status os greater thn or equal to 400
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
