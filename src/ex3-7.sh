#!/bin/bash

read a
mkdir $a
cd $a
touch file0.text
touch file1.text
touch file2.text
touch file3.text
touch file4.text
mkdir file0
mkdir file1
mkdir file2
mkdir file3
mkdir file4

ln -s file0.txt file0
ln -s file1.txt file1
ln -s file2.txt file2
ln -s file3.txt file3
ln -s file4.txt file4
