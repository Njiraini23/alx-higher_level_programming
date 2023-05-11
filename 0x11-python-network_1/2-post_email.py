#!/usr/bin/python3
"""Takes the URL in an email, sends a POST rquest to the URL
with the email as paramtr. Displays the body of the response
coded in utf-8)
Uses the package urllib and sys
email sent with email variable and must use with statement
"""
from sys import argv
import urllib.request
from urllib.parse import urlencode


if __name__ == '__main__':
    url = argv[1]
    value = {'email': argv[2]}
    email = urlencode(value).encode('ascii')
    request = urllib.request.Request(url, email)
    with urllib.request.urlopen(request) as response:
        string = response.read().decode('utf-8')
        print(string)
