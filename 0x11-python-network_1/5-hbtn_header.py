#!/usr/bin/python3
"""
Takes in URL and sends a request to URL and
displays the value of variable X-Request-ID
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
