#!/bin/bash
# getting the size of a respone with curl
curl -s -o /dev/null -w "%{size_download}\n" $1
