#!/bin/bash

read n1 a n2

if [ "$a" = "+" ]
then
	result=`expr $n1 + $n2`
	echo $result
elif [ "$a" = "-" ]
then
	result=`expr $n1 - $n2`
	echo $result
elif [ "$a" = "*" ]
then
	result=`expr $n1 \* $n2`
	echo $result
elif [ "$a" = "/" ]
then
	result=`expr $n1 / $n2`
	echo $result
fi
