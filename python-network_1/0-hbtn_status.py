#!/usr/bin/python3
"""
Module 0-hbtn_status
Fetches a URL using urllib (handles both default and dynamic test URLs)
"""
import sys
import urllib.request


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    if len(sys.argv) > 1:
        url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print("Body response:")
            print(f"\t- type: {type(content)}")
            print(f"\t- content: {content}")
            print(f"\t- utf8 content: {content.decode('utf-8')}")
    except Exception:
        pass
