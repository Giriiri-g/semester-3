#!/bin/bash

file="numbers"

if [ -f "$file" ]; then
    low=$(sort -n "$file" | head -n 1)
    high=$(sort -n "$file" | tail -n 1)

    echo "Lowest number: $low"
    echo "Highest number: $high"
else
    echo "File not found."
fi
