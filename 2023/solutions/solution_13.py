import os

def find_reflection(pattern):
    for i in range(1, len(pattern[0])):
        columns = min(i, len(pattern[0]) - i)
        
        possible_reflection = True
        smudge = False
        
        for j in range(columns):
            for k in range(len(pattern)):
                if not pattern[k][i - j - 1] == pattern[k][i + j]:
                    if not smudge:
                        smudge = True
                    else:
                        possible_reflection = False 
                        break
            if not possible_reflection:
                break 
        
        if possible_reflection and smudge:
            return i
                       
    return None

def transpose(pattern):
    T = [[None for _ in range(len(pattern))] for _ in range(len(pattern[0]))]
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            T[j][i] = pattern[i][j]
    return T   


if __name__ == "__main__":
    test = False
    file = os.getcwd() + "/2023/inputs/" 
    if test:
        file += "test_input_13.txt"
    else:
        file += "input_13.txt"
    
    patterns = [[list(row) for row in pattern.split("\n")] for pattern in open(file).read().split("\n\n")]
    
    summary = 0
    for pattern in patterns:
        reflection = find_reflection(pattern)
        if not reflection:
            reflection = 100 * find_reflection(transpose(pattern))
        summary += reflection
        
    print(summary)