import os

counts = {"red" : 12, "green" : 13, "blue" : 14}

test_answer = 8
filename = os.getcwd() + "/2023/inputs/" + "input_2.txt"

def possible_subset(subset):
    data = subset.split(",")
    for result in data: 
        count, color = result.split()
        if int(count) > counts.get(color):
            return False 
        
    return True
    

def get_game_score(game):
    game_id, games = game.split(":")
    game_id = int(game_id.split()[1])
    
    for subset in games.split(";"):
        if not possible_subset(subset):
            return 0
    return game_id

if __name__ == "__main__":
    total = 0
    with open(filename) as input:
        for game in input:
            total += get_game_score(game)
    print(total)