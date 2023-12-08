import os

test_answer_1 = 2
test_answer_2 = 6



def parse_graph_data(graph_data):
    graph_data = graph_data.split("\n")
    
    graph = dict()
    
    for node in graph_data:
        key, value = node.split(" = ")
        value = tuple(value[1:-1].split(", "))
        graph[key] = value
    
    return graph

  
def get_step_count(graph, instructions, start="AAA", target="ZZZ"):
    steps = 0
    
    current_token = start
    while current_token != target:
        direction = 0 if instructions[steps % len(instructions)] == 'L' else 1
        current_token = graph[current_token][direction]
        steps += 1
    
    return steps
          
          
if __name__ == "__main__":
    test = 0
    file = os.getcwd() + "/2023/inputs/" 
    if test == 1:
        file += "test_input_8_1.txt"
    elif test == 2:
        file += "test_input_8_2.txt"
    else:
        file += "input_8.txt"
    
    instructions, graph_data = open(file).read().split('\n\n')
    graph = parse_graph_data(graph_data)
    
    print(get_step_count(graph, instructions))