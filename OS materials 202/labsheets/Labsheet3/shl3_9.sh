#!/bin/bash

read -p "Enter the Number of Rows (m) for the Matrix A: " m
read -p "Enter the Number of Columns (n) for the Matrix A: " n


declare -A A

echo "Enter Elements for the Matrix A:"
for ((i = 0; i < m; i++)); do
    for ((j = 0; j < n; j++)); do
        read -p "Enter Element at position ($((i)), $((j))): " A["$i,$j"]
    done
done

echo "Transpose of the Matrix A' :"
for ((j = 0; j < n; j++)); do
    for ((i = 0; i < m; i++)); do
        echo -n "${A["$i,$j"]} "
    done
    echo
done
