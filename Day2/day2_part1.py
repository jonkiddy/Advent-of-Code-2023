# Advent of Code 2023 - Day 2 - Part 1
# https://adventofcode.com/2023/day/2

# Initial GitHub Copilot Chat Prompt:
# <Prompt>


import os
import re


def number_of_valid_games(file_path):
    """
    Reads a text file line by line...
    """
    games = []
    with open(file_path, "r") as file:
        for line in file:
            game_id, rounds = line.split(": ")
            id = int(game_id.split(" ")[1])
            rounds = rounds.split("; ")
            rounds = [dict(re.findall(r"(\d+) (\w+)", round)) for round in rounds]
            games.append((int(game_id.split(" ")[1]), rounds))
    total = sum(game[0] for game in games if check_game(game, 12, 13, 14))
    return total


def check_game(game, red, green, blue):
    for round in game[1]:
        if (
            int(round.get("red", 0)) > red
            or int(round.get("green", 0)) > green
            or int(round.get("blue", 0)) > blue
        ):
            return False
    return True


def main():
    # print(number_of_valid_games("Day2/day2_example.txt"))
    print(number_of_valid_games("Day2/day2_input.txt"))
    # The answer is ??? for my input.


if __name__ == "__main__":
    main()
