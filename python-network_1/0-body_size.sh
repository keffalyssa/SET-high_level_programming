#!/bin/bash
# Script that takes a URL, sends a request, and displays the body size in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r'
