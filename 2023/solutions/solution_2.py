import os

test_answer = 8
filename = os.getcwd() + "/2023/inputs/" + "input_2.txt"

def get_game_score(game):
    _, games = game.split(":")
    
    min = {"red" : 0, "green" : 0, "blue" : 0}
    for subset in games.split(";"):
        for color_data in subset.split(","):
            count, color = color_data.split()
            count = int(count)
            if min.get(color) < count:
                min[color] = count
    
    prod = 1
    for key in min.keys():
        prod *= min[key]
    return prod

if __name__ == "__main__":
    total = 0
    with open(filename) as input:
        for game in input:
            total += get_game_score(game)
    print(total)