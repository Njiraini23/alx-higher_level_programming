#!/usr/bin/python3
"""
Python script that takes URL and email addresses
sends POST request to the passed URL
Uses the packages requests and sys
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    response = requests.post(url, data=email)
    print(response.text)
