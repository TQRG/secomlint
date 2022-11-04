#!/bin/bash
value=($(jq -r '.token' "config.json"))

curl -H "Authorization: bearer $value" -X POST -d " \
 { \
   \"query\": \"query { viewer { login }}\" \
 } \
" https://api.github.com/graphql