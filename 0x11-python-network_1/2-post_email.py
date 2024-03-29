#!/usr/bin/python3

"""A URL, and an email address,
sends a POST request to the URL with the email as a parameter.
"""

import urllib.request
import urllib.parse
import sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {"email": argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode("utf-8"))
