#!/bin/bash
# Script that takes a URL, sends a GET request with a custom header variable, and displays the response body
curl -s -H "X-School-User-Id: 98" "$1"
