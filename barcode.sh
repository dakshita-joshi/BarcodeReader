#!/bin/bash
output=flag.txt
for file in $(ls | sort -V).png;
do
    a=`python3 barcode.py "$file"`;
    echo -n $a>>$output
done;
