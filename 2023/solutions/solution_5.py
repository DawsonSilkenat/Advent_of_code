import os
from functools import reduce

test_answer = 35
test_filename = os.getcwd() + "/2023/inputs/" + "test_input_5.txt"
filename = os.getcwd() + "/2023/inputs/" + "input_5.txt"

def parse_seeds(seeds_data):
    return map(int, seeds_data.split()[1:])

def update_seed(seed, maps):
    for dest_start, source_start, num_values in maps:
        diff = seed - source_start
        if 0 <= diff and diff < num_values:
            return dest_start + diff 
    return seed      
    
if __name__ == "__main__":
    test = False
    if test: 
        seeds, *inputs = open(test_filename).read().split('\n\n')
    else:
        seeds, *inputs = open(filename).read().split('\n\n')
    maps = [[[int(v) for v in m.split()] for m in input.split("\n")[1:]] for input in inputs]
    seeds = reduce(lambda s, m: map(lambda x: update_seed(x, m), s), maps, parse_seeds(seeds))
     
    print(min(seeds))
    

          