# Advent of Code 2023 - Day 3 - Part 2
# https://adventofcode.com/2023/day/3

# Initial GitHub Copilot Chat Prompt:
# Prompt 1:
# Each single digit when concatonated with surrounding digits comprises a part number.
# For each '*' determine if it is adjacent or diagonal to exactly two part numbers. If
# it is, multiple both part numbers together and call that a gear_ratio. Then add all
# the gear_ratios. For the sample.txt file, there should be a total of two gear_ratios
# when added together equal 467835.
# Prompt 2:
# I believe there is a bug in the code; the second part number is added to the
# dictionary twice by mistake.

import re
import string

day, part = "3", "2"


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


def calculate_gear_ratios(file_path):
    with open(file_path, "r") as file:
        schematic = [list(line.strip()) for line in file]

    symbols = set(string.printable) - set(string.digits)

    # remove the period symbol from the symbols set
    symbols.remove(".")

    rows, cols = len(schematic), len(schematic[0])

    # Step 1
    part_numbers = [[None] * cols for _ in range(rows)]
    gear_ratios = []

    # Step 2
    for i in range(rows):
        row = "".join(schematic[i])

        # Step 3
        for match in re.finditer(r"\d+", row):
            # Step 4
            num = int(match.group())
            start, end = match.start(), match.end()
            for j in range(start, end):
                part_numbers[i][j] = num

    # Step 5
    for i in range(rows):
        for j in range(cols):
            if schematic[i][j] == "*":
                adjacent_parts = set()  # Change this line
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == dy == 0:
                            continue
                        nx, ny = i + dx, j + dy
                        if (
                            0 <= nx < rows
                            and 0 <= ny < cols
                            and part_numbers[nx][ny] is not None
                        ):
                            adjacent_parts.add(part_numbers[nx][ny])  # And this line
                if len(adjacent_parts) == 2:
                    gear_ratios.append(adjacent_parts.pop() * adjacent_parts.pop())

    return sum(gear_ratios)


def main():
    # Test the sample input
    sample_answer = 467835
    print(f"Day {day} Part {part}")
    answer = calculate_gear_ratios(f"Day{day}/sample.txt")
    if answer == sample_answer:
        print("Sample passed!")
    else:
        print(f"Expected {sample_answer}, got {answer}.")

    # Solve the puzzle input
    print(calculate_gear_ratios(f"Day{day}/input.txt"))
    # The answer is 84584891 for my input.


if __name__ == "__main__":
    main()
