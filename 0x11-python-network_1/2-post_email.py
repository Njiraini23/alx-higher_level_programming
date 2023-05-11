#!/usr/bin/python3
"""Takes the URL in an email, sends a POST rquest to the URL 
with the email as paramtr. Displays the body of the response
coded in utf-8)
Uses the package urllib and sys
email sent with email variable and must use with statement
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
