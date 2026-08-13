#!/bin/bash
# Script that takes in a URL, sends a GET request, and displays the body of a 200 status response
curl -s -L -f "$1"
