#!/usr/bin/python3

"""
given a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys import argv

if __name__ == "__main__":
    the_page = argv[1]
    try:
        with urllib.request.urlopen(the_page) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.code))
