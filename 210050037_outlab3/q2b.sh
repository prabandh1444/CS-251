#!/bin/bash
for file in $1/*
 do 
  echo mv "$file" \
# mv renames the file
    "$(awk -F '[-_]' '{  print $3"-"$4"-20"$2"_"$5}' <<<"$file")"
done
