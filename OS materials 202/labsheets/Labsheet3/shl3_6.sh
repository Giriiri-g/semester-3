#!/bin/bash

read -p "Enter the Number of Elements (n): " n

declare -a arr

for ((i = 0; i < n; i++)); do
    read -p "Enter Element $((i + 1)): " arr[i]
done


sum_=0
for ((i = 0; i < n; i++)); do
    sum_=$((sum_ + arr[i]))
done


average=$(echo "scale=2; $sum_ / $n" | bc)
echo "Average: $average"
