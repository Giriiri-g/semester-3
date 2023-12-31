#!/bin/bash

cd
mkdir -p Test1/Test2/Test3
echo -e "\n\nQuestion 1.a"
(cd Test1/Test2/Test3 && pwd)


ls -l | cat >Test1/Test2/Test3/file1
echo -e "\n\nQuestion 1.b"
ls Test1/Test2/Test3
cat Test1/Test2/Test3/file1

cd Test1/Test2/Test3
echo -e "\n\nQuestion 1.c"
pwd

echo -e "\n\nQuestion 1.d"
tail +2 file1 | rev | cut -d " " -f 1 | rev

echo -e "\n\nQuestion 1.e"
tail +2 file1 | rev | cut -d " " -f 1 | rev | grep -iE '^d'

echo -e "\n\nQuestion 1.f"
tr -s '[:space:]' '\n' < file1

echo -e "\n\nQuestion 1.g"
cd
pwd
