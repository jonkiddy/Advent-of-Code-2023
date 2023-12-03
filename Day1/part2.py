# Advent of Code 2023 - Day 1 - Part 2
# https://adventofcode.com/2023/day/1


import re
from prettytable import PrettyTable

day, part = "1", "2"


def first_and_last(line):
    """
    Parses a line to find the first and last digit, concatenates them together, and
    returns the result as an integer.
    """
    digits = re.findall(r"\d", line.strip())
    return int(digits[0] + digits[-1]) if digits else None


def sum_digits_in_file(file_path):
    """
    Reads a text file line by line, parses each line to find and concatenate the first
    and last digit, stores the result as an integer in a list, and returns the sum of
    all values in the list.
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
    output = PrettyTable(align="l", field_names=["Line", "Parsed Line", "Value"])
    values = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            digits = ""
            i = 0
            for char in line:
                i += 1
                if char.isdigit():
                    digits += char
                else:
                    for key, val in word_to_digit.items():
                        if char == key[0]:
                            if len(line) >= i - 1 + len(key):
                                chars = line[i - 1 : i - 1 + len(key)]
                                if key == chars:
                                    digits += val

            parsed = first_and_last(digits)
            values.append(parsed)
            output.add_row([line, digits, parsed])

    # print(output)
    return sum(values)


def main():
    print(f"Day {day} Part {part}")
    # print(sum_digits_in_file(f"Day{day}/sample.txt"))
    print(sum_digits_in_file(f"Day{day}/input.txt"))
    # The answer is 53539 for my input.


if __name__ == "__main__":
    main()
