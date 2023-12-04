import os 

test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def parse_line(line: str):
    winning_nums, my_nums = line.split("|")
    winning_nums = winning_nums.split()[2:]
    my_nums = my_nums.split()
    return winning_nums, my_nums
    

def solve_line(winning_nums, my_nums):
    matches = 0
    for num in my_nums:
        if num in winning_nums:
            matches += 1
    if matches == 0:
        return 0
    else:
        return 2 ** (matches - 1)

if __name__ == "__main__":
    total = 0
    # input = test_data.split("\n")
    with open(os.getcwd() + "/2023/inputs/input_4.txt") as input:
        for line in input:
            total += solve_line(*parse_line(line))
        
    print(total)