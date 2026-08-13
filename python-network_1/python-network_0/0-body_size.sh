#!/bin/bash
# Script that takes a URL, sends a request, and displays the body size of the response
curl -s "$1" | wc -c
