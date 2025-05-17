#!/bin/bash

req_text="BROAD4CAST"
#Command
output=$(ifconfig)

if [[ "$output" == *"$req_text"* ]]; then
        echo "Success"
else
        echo "Fail"
fi
