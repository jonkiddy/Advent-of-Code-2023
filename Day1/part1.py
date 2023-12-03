# Advent of Code 2023 - Day 1 - Part 1
# https://adventofcode.com/2023/day/1

# Initial GitHub Copilot Chat Prompt:
# "I'd like to write a Python script that reads a text file line by line. For each line,
# I want to find the first and last digit, concatonate them together, and store the
# result as an integer in an array. At the end, I want to sum all the values in the
# array and print the total. I'm using Python 3.12. Can you help me write this script?"


import re

day, part = "1", "1"


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
    digits_array = []
    with open(file_path, "r") as file:
        for line in file:
            parsed_value = parse_line(line)
            if parsed_value is not None:
                digits_array.append(parsed_value)
    return sum(digits_array)


def main():
    print(f"Day {day} Part {part}")
    # print(sum_digits_in_file(f"Day{day}/sample.txt"))
    print(sum_digits_in_file(f"Day{day}/input.txt"))
    # The answer is 55017 for my input.


if __name__ == "__main__":
    main()
