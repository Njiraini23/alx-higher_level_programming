#!/bin/bash
# sends JSON post request to URL passed as first argumnt and display body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
