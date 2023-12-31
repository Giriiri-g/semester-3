#!/bin/bash

echo -e "\n\nQuestion 2"
read -p "Enter the Length of the Rectangle: " l
read -p "Enter the Breadth of the Rectangle: " b

area=$((l * b))
peri=$((2 * (l + b)))

echo "Rectangle Area: $area"
echo "Rectangle Perimeter: $peri"


read -p "Enter the Radius of the Circle: " r

carea=$(echo "scale=2; 3.14 * $r * $r" | bc)
cperi=$(echo "scale=2; 2 * 3.14 * $r" | bc)

echo "Circle Area: $carea"
echo "Circle Circumference: $cperi"
