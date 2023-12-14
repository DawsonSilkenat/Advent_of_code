import os


def calculate_arrangements(row, groups):
    while i < len(row):
        if row[i] == "?":
            if group_index == len(groups) or group_count == groups[group_index]:
                row = row.replace("?", ".", 1)
            elif group_count > 0:
                row = row.replace("?", "#", 1)
            else:
                return calculate_arrangements(row.replace("?", ".", 1), groups, group_index, group_count, i) \
                     + calculate_arrangements(row.replace("?", "#", 1), groups, group_index, group_count, i)
                  
        if row[i] == "#":
            group_count += 1
            if group_index == len(groups) or groups[group_index] < group_count:
                return 0
        else:
            if group_count > 0:
                if group_count != groups[group_index]:
                    return 0
                group_count = 0
                group_index += 1
        
        i += 1
    
    if group_index == len(groups) or (group_index == len(groups) - 1 and group_count == groups[group_index]):
        return 1
    else:
        return 0

def unfold(row, groups):
    return "?".join([row] * 5), groups * 5   


if __name__ == "__main__":
    test = False 
    file = os.getcwd() + "/2023/inputs/" 
    if test:
        file += "test_input_12.txt"
    else:
        file += "input_12.txt"
        
    document = [[y[0], [int(z) for z in y[1].split(",")]] for y in map(lambda x: x.split(),open(file).read().split("\n"))]
    
    count = 0
    for row, groups in document:
        count += calculate_arrangements(*unfold(row, groups))
        
    print(count)
    
    

    
    

