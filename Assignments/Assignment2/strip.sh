#!/bin/bash

k="$1"
m="$2"
filename="$3" 

cat $filename | head -n -$m | tail -n +$k


