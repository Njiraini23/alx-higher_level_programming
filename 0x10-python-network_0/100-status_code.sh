#!/bin/bash
# Sends requests to URL, only displays status of code
curl -s -o /dev/null -w "%{http_code}" "$1"
