#!/bin/bash
# Makes request to 0.0.0.0:500/catch_me on port 5000 with a message You got me
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
