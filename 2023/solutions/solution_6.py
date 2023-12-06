import os

test_answer = 71503
test_filename = os.getcwd() + "/2023/inputs/" + "test_input_6.txt"
filename = os.getcwd() + "/2023/inputs/" + "input_6.txt"

def calculate_distance(hold_time, total_time):
    return hold_time * (total_time - hold_time) 


def calculate_possible_solutions(time, distance):
    ways_to_win = 0
    for t in range(time + 1):
        if calculate_distance(t, time) > distance:
            ways_to_win += 1
    return ways_to_win


if __name__ == "__main__":
    test = False
    if test: 
        time, distance = open(test_filename).read().split('\n')
    else:
        time, distance = open(filename).read().split('\n')
    
    time = int("".join(time.split()[1:]))  
    distance = int("".join(distance.split()[1:]))
    
    print(calculate_possible_solutions(time, distance))