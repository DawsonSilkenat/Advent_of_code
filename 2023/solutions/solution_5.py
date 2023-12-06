import os
from functools import reduce

test_answer = 35
test_filename = os.getcwd() + "/2023/inputs/" + "test_input_5.txt"
filename = os.getcwd() + "/2023/inputs/" + "input_5.txt"

def parse_seeds(seeds_data):
    seeds_data = map(int, seeds_data.split()[1:])
    as_pairs = []
    for start in seeds_data:
        num_values = seeds_data.__next__()
        as_pairs.append([start, num_values])
    return as_pairs
        

def update_seed(seed, maps):
    # Seed will be of the form [start, r]
    # return a list of the form [[start, r], [start, r]] for each of the new ranges
    
    unprocessed = seed
    processed = []
    
    for dest_start, source_start, num_values in maps:
        new_uprocessed = []
        for seed in unprocessed:
            left, overlap, right = get_segments(seed, [source_start, num_values])
            if left:
                new_uprocessed.append(left)
            if right:
                new_uprocessed.append(right)
            if overlap:
                diff = overlap[0] - source_start
                processed.append([dest_start + diff, overlap[1]])
        
        unprocessed = new_uprocessed
    
    
    return processed + unprocessed     
  
  
def get_segments(overlap_of, overlap_with):
    
    overlap_of_end = overlap_of[0] + overlap_of[1] - 1
    overlap_with_end = overlap_with[0] + overlap_with[1] - 1
    
    if overlap_of_end < overlap_with[0]:
        return overlap_of, [], []
    if overlap_with_end < overlap_of[0]:
        return [], [], overlap_of
    
    
    left = [overlap_of[0], overlap_with[0] - overlap_of[0]]
    if left[1] < 1:
        left = []
    
    overlap_start = max(overlap_of[0], overlap_with[0])
    overlap_end = min(overlap_of_end, overlap_with_end)
    overlap = [overlap_start, overlap_end - overlap_start + 1]
    if overlap[1] < 1:
        overlap = []
        
    right = [overlap_end + 1, overlap_of_end - overlap_end]
    if right[1] < 1:
        right = [] 
    
    
    return left, overlap, right

    
if __name__ == "__main__":
    test = False
    if test: 
        seeds, *inputs = open(test_filename).read().split('\n\n')
    else:
        seeds, *inputs = open(filename).read().split('\n\n')
    
    maps = [[[int(v) for v in m.split()] for m in input.split("\n")[1:]] for input in inputs]
    seeds = reduce(update_seed, maps, parse_seeds(seeds))
     
    print(min(map(lambda x: x[0], seeds)))
    

          