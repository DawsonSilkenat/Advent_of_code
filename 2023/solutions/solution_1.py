import os

test_answer = 142
filename = os.getcwd() + "/2023/inputs/" + "input_1.txt"

def get_number(line):
    first = None
    last = None 
    for char in line:
        if char.isdigit():
            if first is None:
                first = char 
            last = char 
    return int(first + last)

if __name__ == "__main__":
    total = 0
    with open(filename) as input:
        for line in input:
            total += get_number(line)
    print(total)