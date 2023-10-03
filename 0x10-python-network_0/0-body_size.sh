#!/bin/bash
# getting the size of a respone with curl
curl -s $1 | wc -c
