import os 

test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def parse_card(line: str):
    winning_nums, my_nums = line.split("|")
    winning_nums = winning_nums.split()[2:]
    my_nums = my_nums.split()
    return winning_nums, my_nums
    

def card_winnings(winning_nums, my_nums):
    matches = 0
    for num in my_nums:
        if num in winning_nums:
            matches += 1
    return matches

if __name__ == "__main__":
    # input = test_data.split("\n")    

    card_counts = []
    with open(os.getcwd() + "/2023/inputs/input_4.txt") as input:
    # for _ in range(1):
        for _ in input:
            card_counts.append(1)
            
    current_card = 0

    with open(os.getcwd() + "/2023/inputs/input_4.txt") as input:
    # for _ in range(1): 
        for line in input:
            result = card_winnings(*parse_card(line))
            for i in range(result):
                card_counts[current_card + i + 1] += card_counts[current_card]
            
            current_card += 1
            

    print(sum(card_counts))