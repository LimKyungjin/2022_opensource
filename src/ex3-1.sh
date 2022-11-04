#!/bin/bash

i=1
read number
while [ $i -le $number ]
do
	echo "hello world"
	i=`expr $i + 1`
done
exit 0
