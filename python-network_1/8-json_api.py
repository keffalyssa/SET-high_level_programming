#!/usr/bin/python3
"""
Module 8-json_api
Takes in a letter, sends a POST request to search_user
with the letter as a parameter, and handles JSON responses.
"""
import sys
import requests


if __name__ == '__main__':
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    payload = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
