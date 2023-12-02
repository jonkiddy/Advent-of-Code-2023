# Advent of Code 2023 - Day 1 - Part 1
# https://adventofcode.com/2023/day/1

# Initial GitHub Copilot Chat Prompt:
# "I'd like to write a Python script that reads a text file line by line. For each line,
# I want to find the first and last digit, concatonate them together, and store the
# result as an integer in an array. At the end, I want to sum all the values in the
# array and print the total. I'm using Python 3.12. Can you help me write this script?"


import os  # Operating System Module
import re  # Regular Expression Module

from prettytable import PrettyTable


def parse_line(line):
    """
    Parses a line to find the first and last digit, concatenates them together, and
    returns the result as an integer.
    """
    digits = re.findall(r"\d", line.strip())
    return int(digits[0] + digits[-1]) if digits else None


def sum_digits_in_file(file_path):
    """
    Reads a text file line by line, parses each line to find and concatenate the first
    and last digit, stores the result as an integer in an array, and returns the sum of
    all values in the array.
    """
    word_to_digit = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    table = PrettyTable(["Line", "New Line", "Parsed Line"])
    digits_array = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                words_and_digits = re.findall(
                    r"\b" + "|".join(word_to_digit.keys()) + r"\b|\d+", line
                )
                print(words_and_digits)
                new_line = "".join(
                    word_to_digit[word] if word in word_to_digit else word
                    for word in words_and_digits
                )
                parsed_line = parse_line(new_line)
                table.add_row([line, new_line, parsed_line])
                digits_array.append(parsed_line)
    # print(table)
    return sum(digits_array)


def main():
    # total = sum_digits_in_file("day1_input.txt")
    total = sum_digits_in_file("day1_temp.txt")
    print(total)


if __name__ == "__main__":
    main()
