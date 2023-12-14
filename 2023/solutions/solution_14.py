import os
from functools import reduce


def spins(platform, num_spins=1000000000, test_spins=500):
    add = lambda x, y: x + y
    history = []
    
    for _ in range(test_spins):
        before = [[tile for tile in row] for row in platform]
        for _ in range(4):
            roll_platform_north(platform)
            platform = rotate_clockwise(platform) 
        
        # Steady state check
        if all(map(lambda x: x[0] == x[1], zip(reduce(add, before), reduce(add, platform)))):
            print("steady state")
            break
        
        history.append(calculate_load(platform))  
    
    pattern = history[len(history) - get_pattern_length(history):]
    return pattern[(num_spins - test_spins - 1) % len(pattern)]


def rotate_clockwise(platform):
    return mirror(transpose(platform))


def transpose(platform):
    T = [[None for _ in range(len(platform))] for _ in range(len(platform[0]))]
    for i in range(len(platform)):
        for j in range(len(platform[0])):
            T[j][i] = platform[i][j]
    return T  


def mirror(platform):
    return [[row[i] for i in reversed(range(len(row)))] for row in platform]


def get_pattern_length(sequence):
    for i in range(2, len(sequence)):
        is_pattern = True
        for j in range(i):
            if not sequence[-i * 2 + j] == sequence[-i + j]:
                is_pattern = False
                break
        if is_pattern:
            return i
    

def roll_platform_north(platform):
    for i in range(1, len(platform)):
        for j in range(len(platform[i])):
            if platform[i][j] == "O":
                roll_rock_north(platform, i, j)                      
    return platform


def roll_rock_north(platform, i, j):
    while i > 0 and platform[i - 1][j] == ".":
            platform[i - 1][j] = "O"
            platform[i][j]  = "."
            i -= 1 

    
def calculate_load(platform):
    total = 0
    for i in range(1, len(platform) + 1):
        total += i * count_rocks(platform[-i])
    return total


def count_rocks(row):
    return sum([tile == "O" for tile in row])       


if __name__ == "__main__":
    test = 0
    file = os.getcwd() + "/2023/inputs/" 
    if test == 1:
        file += "test_input_14_1.txt"
    elif test == 2:
        file += "test_input_14_2.txt"
    else:
        file += "input_14.txt"
    
    print(spins([[tile for tile in row]for row in open(file).read().split("\n")]))
    