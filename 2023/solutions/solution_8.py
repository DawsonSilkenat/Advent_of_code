import os
from functools import reduce

test_answer_1 = 2
test_answer_2 = 6


def parse_graph_data(graph_data):
    graph_data = graph_data.split("\n")
    
    graph = dict()
    starts = []
    
    for node in graph_data:
        key, value = node.split(" = ")
        value = tuple(value[1:-1].split(", "))
        graph[key] = value
        
        if key[-1] == "A":
            starts.append(key)
    
    return graph, starts

  
def get_step_count(graph, instructions, start):
    steps = 0
    
    current_token = start
    while not current_token[-1] == "Z":
        direction = 0 if instructions[steps % len(instructions)] == 'L' else 1
        current_token = graph[current_token][direction]
        steps += 1
    
    return steps

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a
    if b > a:
        return gcd(b, a)
    return gcd(b, a % b)        
          
if __name__ == "__main__":
    test = 0
    file = os.getcwd() + "/2023/inputs/" 
    if test == 1:
        file += "test_input_8_1.txt"
    elif test == 2:
        file += "test_input_8_2.txt"
    elif test == 3:
        file += "test_input_8_3.txt"
    else:
        file += "input_8.txt"
    
    instructions, graph_data = open(file).read().split('\n\n')
    graph, starts = parse_graph_data(graph_data)
    
    print(reduce(lcm, [get_step_count(graph, instructions, start) for start in starts]))