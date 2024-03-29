#!/usr/bin/python3

"""A script that takes in a URL, and an email, sends a POST request
to the passed URL with the email as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    url_1 = sys.argv[2]
    payload = {'email': url_1}
    respond = requests.post(url, data=payload)
    print(respond.text)
