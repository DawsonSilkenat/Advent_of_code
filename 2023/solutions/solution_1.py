import os

test_answer = 281
filename = os.getcwd() + "/2023/inputs/" + "input_1.txt"

str_digits = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}


def get_number(line):
    first = None
    last = None 
    for i in range(len(line)):
        char = line[i]
        for k in str_digits.keys():
            if line[i : i + len(k)] == k:
                char = str_digits[k]
                break
        
        
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