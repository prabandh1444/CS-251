#!/bin/bash
awk '{for(i = 1; i <= NF; i++){P[$i]++}} END {for(k in P) if(P[k] >= 1) {print k , P[k]}}' $1/*.txt | sort
