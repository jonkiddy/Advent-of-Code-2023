#!/bin/bash

# Iterate over each directory
for dir in */ ; do
    # Skip if the directory is named "Template"
    if [ "$dir" == "Template/" ]; then
        continue
    fi
    # Check if the directory contains Python files
    if ls $dir*.py 1> /dev/null 2>&1; then
        # If Python files are found, run them
        for file in $dir*.py; do
            python $file
        done
    fi
done