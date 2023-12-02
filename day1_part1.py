# Advent of Code 2023 - Day 1 - Part 1
# https://adventofcode.com/2023/day/1

# GitHub Copilot Chat Prompt:
# "I'd like to write a Python script that reads a text file line by line. For each line,
# I want to find the first and last digit, concatonate them together, and store the
# result as an integer in an array. At the end, I want to sum all the values in the
# array and print the total. I'm using Python 3.12. Can you help me write this script?"

import os
import re  # Regular Expression Module


def my_function():
    digits_array = []
    with open("day1_input.txt", "r") as file:
        for line in file:
            digits = re.findall(r"\d", line.strip())
            if digits:
                digits_array.append(int(digits[0] + digits[-1]))
    return sum(digits_array)


def main():
    total = my_function()
    print(total)


if __name__ == "__main__":
    main()
