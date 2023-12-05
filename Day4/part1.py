# Advent of Code 2023 - Day 4 - Part 1
# https://adventofcode.com/2023/day/4

# Initial GitHub Copilot Chat Prompt:
# I have a list of scratchcards, each represented as a string. Each string contains
# two lists of numbers separated by a vertical bar (|). The first list represents the
# winning numbers, and the second list represents the numbers you have.
# Calculate the total score of all scratchcards. The score for each card is calculated
# as follows: the first match between your numbers and the winning numbers makes the
# card worth one point, and each match after the first doubles the point value of that
# card. Solve for the sample puzzle input.

import os
import re

day, part = "4", "1"

# Sample Puzzle Input:
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11


def calc_total_score(file_path):
    """
    Reads a text file line by line and calculates the total score of all cards.
    """
    total_score = 0
    with open(file_path, "r") as file:
        for line in file:
            _, numbers = line.split(":")
            winning_numbers, my_numbers = numbers.split("|")
            winning_numbers = set(map(int, winning_numbers.split()))
            my_numbers = set(map(int, my_numbers.split()))
            matches = winning_numbers & my_numbers
            if matches:
                score = 2 ** (len(matches) - 1)
                total_score += score
    return total_score


def main():
    # Test the sample input
    sample_answer = 13
    print(f"Day {day} Part {part}")
    answer = calc_total_score(f"Day{day}/sample.txt")
    if answer == sample_answer:
        print("Sample passed!")
    else:
        print(f"Expected {sample_answer}, got {answer}.")

    # Solve the puzzle input
    print(calc_total_score(f"Day{day}/input.txt"))
    # The answer is 20855 for my input.


if __name__ == "__main__":
    main()
