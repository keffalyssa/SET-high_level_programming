#!/usr/bin/python3
"""
Module 4-hbtn_status
Fetches a status URL using the requests package, supporting optional arguments
"""
import sys
import requests


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    if len(sys.argv) > 1:
        url = sys.argv[1]
    
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
