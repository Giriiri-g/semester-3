#!/bin/bash



echo -e "Question 1.a\n"
read -p "Enter your Name: " name
read -p "Enter the Program Name: " program_name
read -p "Enter your Enrollment Number: " enrollment_number

echo "Name: $name"
echo "Program Name: $program_name"
echo "Enrollment Number: $enrollment_number"


echo -e "\n\nQuestion 1.b"
read -p "Enter the first integer: " num1
read -p "Enter the second integer: " num2
read -p "Enter the third integer: " num3
read -p "Enter the fourth integer: " num4

let sum=num1+num2+num3+num4
average=$(echo "scale=3; $sum / 4" | bc)
let product=num1*num2*num3*num4

echo "Sum: $sum"
echo "Average: $average"
echo "Product: $product"


echo -e "\n\nQuestion 1.c"
read -p "Enter a Number: " number

if (($number % 2 == 0))
then
    echo "The Number $number is Even."
else
    echo "The Number $number is Odd."
fi


echo -e "\n\nQuestion 1.d"

read -p "Enter the value of Var1: " var1
read -p "Enter the value of Var2: " var2

temp=$var1
var1=$var2
var2=$temp

echo "After exchanging values:"
echo "Variable1: $var1"
echo "Variable2: $var2"


echo -e "\n\nQuestion 1.e"

read -p "Enter the File name: " file
read -p "Enter the Number to search: " val

grep "$val" "$file"




echo -e "\n\nQuestion 1.f"
read -p "Enter the First String: " str1
read -p "Enter the Second String: " str2

res="$str1$str2"

length=${#res}

echo "Concatenated String: $res"
echo "Length of Concatenated String: $length"



echo -e "\n\nQuestion 1.g"
read -p "Enter the First File Name: " file1
read -p "Enter the Second File Name: " file2
cat "$file1" "$file2"


echo -e "\n\nQuestion 1.h"
sleep 5
echo "Current time: $(date)"
