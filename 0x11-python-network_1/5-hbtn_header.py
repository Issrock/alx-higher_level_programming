#!/usr/bin/python3

"""
URL as the parameter, sends a request to the URL
and displays the value
"""

import requests
import sys

if __name__ == "__main__":
    the_page = sys.argv[1]
    r = requests.get(the_page)
    print(r.headers.get("X-Request-Id"))
