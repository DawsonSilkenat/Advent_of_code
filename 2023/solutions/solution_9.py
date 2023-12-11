import os


def get_next_value(seq):
    if all(map(lambda x: x == 0, seq)):
        return 0 
    
    return seq[-1] + get_next_value(get_next_row(seq))


def get_next_row(seq):
    next_row = []
    for i in range(len(seq) - 1):
        next_row.append(seq[i + 1] - seq[i])
    return next_row
        

if __name__ == "__main__":
    test = False
    file = os.getcwd() + "/2023/inputs/" 
    if test:
        file += "test_input_9.txt"
    else:
        file += "input_9.txt"
    
    value_sequences = [[int(v) for v in value.split()] for value in open(file).read().split("\n")]
    for seq in value_sequences:
        seq.reverse()
    
    print(sum(map(get_next_value, value_sequences)))
    