import re
import numpy as np


def process_game1(key1):
    games = read_games()
    possible_ids = []
    for game in games:
        id = re.findall(r'\d+', game.split(":")[0])
        cube_sets = re.findall(r'[0-9]+ [a-z]*', game.split(":")[-1])
        valid = True
        for cube_set in cube_sets:
            number, color = cube_set.split(' ')

            if int(number) > key1[color]:
                valid = False

        if valid:
            possible_ids.append(int(id[0]))

    return sum(possible_ids)


def process_game2():
    games = read_games()
    powers = []
    for game in games:
        min_values = {"red": 1, "green": 1, "blue": 1}
        cube_sets = re.findall(r'[0-9]+ [a-z]*', game.split(":")[-1])
        for cube_set in cube_sets:
            number, color = cube_set.split(' ')

            if int(number) > min_values[color]:
                min_values[color] = int(number)

        powers.append(np.prod(list(min_values.values())))

    return sum(powers)


def read_games():
    return open("games.txt", 'r').readlines()


if __name__ == "__main__":
    key1 = {"red": 12, "green": 13, "blue": 14}
    print("Answer1: ", process_game1(key1))
    print("Answer2: ", process_game2())
    print("Execution Successful")

