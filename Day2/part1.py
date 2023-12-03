# Advent of Code 2023 - Day 2 - Part 1
# https://adventofcode.com/2023/day/2

# Initial GitHub Copilot Chat Prompt (which wasn't very helpful):
# "I'm working on the Advent of Code 2023, Day 2, Part 1 problem. Please create a Python
# script that reads game data from a file and calculates the sum of the game IDs for
# which the game would be possible with a certain number of red, green, and blue cubes."


import re

day, part = "2", "1"


def number_of_valid_games(file_path):
    """
    Reads game data from a file and calculates the sum of the game IDs for which the game.
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
    total = sum(game[0] for game in games if check_game(game, 12, 13, 14))
    return total


def check_game(game, red, green, blue):
    """
    Checks if a game is possible with a certain number of red, green, and blue cubes.
    """
    for round in game[1]:
        if (
            int(round.get("red", 0)) > red
            or int(round.get("green", 0)) > green
            or int(round.get("blue", 0)) > blue
        ):
            return False
    return True


def main():
    print(f"Day {day} Part {part}")
    # print(number_of_valid_games(f"Day{day}/sample.txt"))
    print(number_of_valid_games(f"Day{day}/input.txt"))
    # The answer is 2913 for my input.


if __name__ == "__main__":
    main()
