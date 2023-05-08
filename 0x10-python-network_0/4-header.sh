#!/bin/bash
# takes URL, snds GET rquest to URL and displays body
curl -sH "X-School-User-Id: 98" "${1}"
