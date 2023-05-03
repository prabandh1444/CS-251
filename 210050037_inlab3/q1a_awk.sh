#!/bin/bash
# $1 is the name of directory
awk '{for(i = 1; i <= NF; i++) {A[$i]++}} END {for(k in A) if(A[k] >= 1){counter++} print counter}' $1/*.txt







