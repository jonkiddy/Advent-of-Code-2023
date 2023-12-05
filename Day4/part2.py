# Advent of Code 2023 - Day 4 - Part 2
# https://adventofcode.com/2023/day/4

# Initial GitHub Copilot Chat Prompt:
# <Prompt>

import os
import re

day, part = "4", "2"


def calc_total_cards(file_path):
    """
    Reads a text file line by line and calculates the total number of cards, including
    the original and copied cards.
    """
    cards = []
    with open(file_path, "r") as file:
        for line in file:
            _, numbers = line.split(":")
            winning_numbers, my_numbers = numbers.split("|")
            winning_numbers = set(map(int, winning_numbers.split()))
            my_numbers = set(map(int, my_numbers.split()))
            cards.append((winning_numbers, my_numbers))

    i = 0
    while i < len(cards):
        winning_numbers, my_numbers = cards[i]
        matches = winning_numbers & my_numbers
        for j in range(min(len(matches), len(cards) - i - 1)):
            cards.append(cards[i + j + 1])
        i += 1

    return len(cards)


def main():
    # Test the sample input
    sample_answer = 30
    print(f"Day {day} Part {part}")
    answer = calc_total_cards(f"Day{day}/sample.txt")
    if answer == sample_answer:
        print("Sample passed!")
    else:
        print(f"Expected {sample_answer}, got {answer}.")

    # Solve the puzzle input
    # print(calc_total_cards(f"Day{day}/input.txt"))
    # The answer is ??? for my input.


if __name__ == "__main__":
    main()
