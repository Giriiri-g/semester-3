#!/bin/bash

read -p "Enter the Number of Rows (m) for both matrices: " m
read -p "Enter the Number of Columns (n) for both matrices: " n

# Declare two-dimensional arrays
declare -A matrix1
declare -A matrix2

echo "Enter elements for the first matrix:"
for ((i = 0; i < m; i++)); do
    for ((j = 0; j < n; j++)); do
        read -p "Enter element at position ($((i)), $((j))) for the first matrix: " matrix1["$i,$j"]
    done
done

echo "Enter elements for the second matrix:"
for ((i = 0; i < m; i++)); do
    for ((j = 0; j < n; j++)); do
        read -p "Enter element at position ($((i)), $((j))) for the second matrix: " matrix2["$i,$j"]
    done
done

# Adding the matrices and printing the result
echo "Resultant matrix (sum of matrices):"
for ((i = 0; i < m; i++)); do
    for ((j = 0; j < n; j++)); do
        result=$((matrix1["$i,$j"] + matrix2["$i,$j"]))
        echo -n "$result "
    done
    echo
done
