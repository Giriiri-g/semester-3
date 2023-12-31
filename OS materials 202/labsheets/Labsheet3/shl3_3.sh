#!/bin/bash
echo "Menu:"
echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"
echo "5. Modulus"
echo "6. Increment"
echo "7. Decrement"
read -p "Enter the First Number: " num1
read -p "Enter the Second Number: " num2
read -p "Enter the Operation (1-7): " op
case $op in
    1)  res=$((num1 + num2)); echo "Sum: $res";;
    2)  res=$((num1 - num2)); echo "Difference: $res";;
    3)  res=$((num1 * num2)); echo "Product: $res";;
    4)  if (( $(echo "$num2 != 0" | bc -l) )); then
            res=$(echo "scale=2; $num1 / $num2" | bc)
            echo "Quotient: $res"
        else
            echo "Cannot divide by zero."
        fi;;
    5)  if (( $(echo "$num2 != 0" | bc -l) )); then
            res=$((num1 % num2))
            echo "Remainder: $res"
        else
            echo "Cannot find remainder when dividing by zero."
        fi;;
    6)  res=$((num1 + 1)); echo "Increment of $num1: $res";;
    7)  res=$((num1 - 1)); echo "Decrement of $num1: $res";;
    *)  echo "Invalid operation.";;
esac
