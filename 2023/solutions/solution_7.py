import os

test_answer = 6440
test_filename = os.getcwd() + "/2023/inputs/" + "test_input_7.txt"
filename = os.getcwd() + "/2023/inputs/" + "input_7.txt"

cards = "AKQT98765432J"

def get_card_counts(hand):
    counts = dict()
    for char in hand:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
    

def get_hand_type(hand):
    counts = get_card_counts(hand)
    jokers = counts.pop('J', 0)
    counts = list(counts.values())
    counts.sort(reverse=True)
    
    if counts:
        counts[0] += jokers
    else:
        counts.append(jokers)
    
    match counts:
        case [5]:
            return 6
        case [4, 1]:
            return 5
        case [3, 2]:
            return 4
        case [3, 1, 1]:
            return 3
        case [2, 2, 1]:
            return 2
        case [2, 1, 1, 1]:
            return 1
        case default: 
            return 0
    
def get_card_values(hand):
    values = []
    for card in hand:
        values.append(len(cards) - cards.index(card))   
        
    return values



if __name__ == "__main__":
    test = False
    hand_data = map(lambda x: x.split(), open(test_filename if test else filename).read().split('\n'))
    hand_data = map(lambda x: [get_hand_type(x[0]), get_card_values(x[0]), int(x[1])], hand_data)  
    hand_data = list(map(lambda x: x[2], sorted(hand_data)))
    
    sum = 0
    for i in range(len(hand_data)):
        sum += (i + 1) * hand_data[i]
        
    print(sum)
        