#!/bin/bash

pattern=''
word=''

file=$1
while read line1; do
    m=0
    for word1 in $line1; do
        if [[ $word1 == '#@$' ]]; then
          line=($line1)
          word=${line[m+1]}
          break 2
        fi
        m=$((m+1)) 
    done
done <$file
for((j=1;j<$2;j++)) do
  while read line1; do
      i=0
      for word1 in $line1; do
          if [[ $word1 == $word ]]; then
            line=($line1)
            pattern=${line[i+1]}
            if [[ $pattern =~ ['!@#$%^&*'] ]]; then
                word=${line[i+2]}
                break 2  
            fi  
         fi
          i=$((i+1)) 
      done
  done <$file
done

while read line1; do
    k=0
    for word1 in $line1; do
        if [[ $word1 == $word ]]; then
          line=($line1)
          pattern=${line[k+1]}
          if [[ $pattern =~ ['!@#$%^&*'] ]]; then
            break 2
          fi  
        fi
        k=$((k+1)) 
    done
done <$file



echo "Last Word found: $word"
echo "Last Pattern found: $pattern"
