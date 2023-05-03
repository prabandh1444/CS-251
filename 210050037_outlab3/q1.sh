#!/bin/bash
file=$1
regex="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
while read line; do
        if [[ $line =~ $regex ]]; then
          echo "$line" >> valid.txt
        fi
done <$file
