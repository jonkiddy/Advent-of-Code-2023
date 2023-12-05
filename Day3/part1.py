# Advent of Code 2023 - Day 3 - Part 1
# https://adventofcode.com/2023/day/3

# Initial GitHub Copilot Chat Prompt:
# Prompt 1:
# * Import the necessary libraries: re, and string.
# * Define the sum_part_numbers function that takes a file path as an argument.
# * Inside the function, open the file and read its contents into a list of lists,
#   where each inner list represents a row in the schematic.
# * Define a set of symbols to be any printable character that is not a digit.
# * Initialize the total sum of part numbers to 0.
# * Iterate over each row in the schematic.
# * For each row, convert it to a string and use a regular expression to find all
#   sequences of digits.
# * For each match, convert the matched string to an integer and store it along with
#   its start and end positions in a list of part numbers.
# * After collecting all part numbers, iterate over the list.
# * For each part number, check the cells around its start and end positions in the
#   schematic for symbols.
# * If a symbol is found, add the part number to the total sum.
# * After iterating over all part numbers, return the total sum.
# * Call the sum_part_numbers function with the path to the input file and print the
#   returned sum.
# Prompt 2:
# If a set of numbers are in a sequence, they should be catenated together and then
# turned into an int. Then the adjacent check should be applied to the location
# of the entire number as a whole, not just individual locations of each digit.
# Prompt 3:
# Can you change the symbol set to include any symbole except 0-9?

import re
import string

day, part = "3", "1"


# Sample Input
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..


def sum_part_numbers(file_path):
    with open(file_path, "r") as file:
        schematic = [list(line.strip()) for line in file]

    symbols = set(string.printable) - set(string.digits)

    # remove the period symbol from the symbols set
    symbols.remove(".")

    rows, cols = len(schematic), len(schematic[0])
    total = 0

    # Step 1
    part_numbers = []

    # Step 2
    for i in range(rows):
        row = "".join(schematic[i])

        # Step 3
        for match in re.finditer(r"\d+", row):
            # Step 4
            num = int(match.group())
            start, end = match.start(), match.end()
            part_numbers.append((num, i, start, end))

    # Step 5
    for num, i, start, end in part_numbers:
        for dx in [-1, 0, 1]:
            for dy in range(start - 1, end + 1):
                if (
                    0 <= i + dx < rows
                    and 0 <= dy < cols
                    and schematic[i + dx][dy] in symbols
                ):
                    # Step 7
                    # print(f"Found {num} at ({i}, {dy})")
                    total += num
                    break
            else:
                continue
            break

    return total


def main():
    # Test the sample input
    print(f"Day {day} Part {part}")
    answer = sum_part_numbers(f"Day{day}/sample.txt")
    if answer == 4361:
        print("Sample passed!")
    else:
        print(f"Expected 4361, got {answer}.")

    # Solve the puzzle input
    print(sum_part_numbers(f"Day{day}/input.txt"))
    # The answer is 540025 for my input.


if __name__ == "__main__":
    main()
