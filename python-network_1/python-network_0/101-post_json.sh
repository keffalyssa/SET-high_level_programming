#!/bin/bash
# Script that sends a JSON POST request with the contents of a file passed as the second argument
curl -s -H "Content-Type: application/json" -d "@$2" "$1"
