import os 


def hash(step):
    value = 0
    for char in step:
        value += ord(char)
        value *= 17 
        value %= 256
    return value
        

if __name__ == "__main__":
    test = False
    file = os.getcwd() + "/2023/inputs/" 
    if test:
        file += "test_input_15.txt"
    else:
        file += "input_15.txt"
    
    steps = open(file).read().split(",")
    value = 0
    for step in steps:
        value += hash(step)
    print(value)