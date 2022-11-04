#!/bin/bash

echo "program start!"
echo "in function"

files(){
   ls $1
}

files $1

echo "program end"

exit 0
