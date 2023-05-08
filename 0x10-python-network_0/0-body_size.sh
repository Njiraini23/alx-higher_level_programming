#!/bin/bash
# Takes URL and displays size in bytes
curl -s "$1" | wc -c
