#!/usr/bin/python3
"""
Module 1-hbtn_header
Takes in a URL, sends a request, and displays the value
of the X-Request-Id variable in the response header.
"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')
        print(request_id)
