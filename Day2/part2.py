# Advent of Code 2023 - Day 2 - Part 2
# https://adventofcode.com/2023/day/2

import os
import re

day, part = "2", "2"


def number_of_valid_games(file_path):
    """
    Reads game data from a file and calculates the sum of the power of the minimum sets of cubes for each game.
    """
    games = []
    with open(file_path, "r") as file:
        for line in file:
            game_id, rounds = line.split(": ")
            id = int(game_id.split(" ")[1])
            rounds = rounds.split("; ")
            rounds = [re.findall(r"(\d+) (\w+)", round) for round in rounds]
            rounds = [
                {
                    color: sum(int(count) for count, color_ in round if color_ == color)
                    for color in ["red", "green", "blue"]
                }
                for round in rounds
            ]
            games.append((id, rounds))
    total = sum(check_game(game) for game in games)
    return total


def check_game(game):
    """
    Calculates the minimum number of cubes of each color that could have been in the bag to make the game possible.
    """
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for round in game[1]:
        for color in ["red", "green", "blue"]:
            min_cubes[color] = max(min_cubes[color], int(round.get(color, 0)))
    return min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]


def main():
    # Test the sample input
    sample_answer = 2286
    print(f"Day {day} Part {part}")
    answer = number_of_valid_games(f"Day{day}/sample.txt")
    if answer == sample_answer:
        print("Sample passed!")
    else:
        print(f"Expected {sample_answer}, got {answer}.")

    # Solve the puzzle input
    print(number_of_valid_games(f"Day{day}/input.txt"))
    # The answer is 55593 for my input.


if __name__ == "__main__":
    main()
