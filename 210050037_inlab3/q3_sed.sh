#!/bin/bash
sed -i 's/\./$/g' $1
sed -z 's/\$\n/:)\n/g' $1

