import os

test_answer = 288
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
        times, distances = open(test_filename).read().split('\n')
    else:
        times, distances = open(filename).read().split('\n')
    
    times = map(int, times.split()[1:])  
    distances = map(int, distances.split()[1:])
    
    product = 1
    for t, d in zip(times, distances):
        product *= calculate_possible_solutions(t, d)
        
    print(product)