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

    total_cards = len(cards)
    copied_cards = []
    for i in range(total_cards):
        winning_numbers, my_numbers = cards[i]
        matches = len(winning_numbers & my_numbers)
        print(f"Card {i + 1} has {matches} matches.")
        for _ in range(matches):
            if i + 1 < total_cards:
                copied_cards.append(cards[i + 1])

    cards.extend(copied_cards)
    total_cards = len(cards)

    return total_cards


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
