#!/usr/bin/python3
"""
Module 5-hbtn_header
Takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header.
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
