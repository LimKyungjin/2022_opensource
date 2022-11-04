#!/bin/bash

read w h

normal=`expr 10000 \* $w / $h / $h` 

if [ 1 -eq "$(echo "${normal} < 18.5"| bc)" ];
then
	echo "low"
elif [ ${normal} -lt 23 ];
then
	echo "normal"
else 
	echo "high"
fi
exit 0
	
