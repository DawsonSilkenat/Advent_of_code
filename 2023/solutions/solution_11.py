import os

def solve_map(galaxies_map):
    galaxies, row_contains, column_contains = get_map_details(galaxies_map)
    
    total = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            total += get_distance(galaxies[i], galaxies[j], row_contains, column_contains)
    return total
        

def get_map_details(galaxies_map):
    galaxies = []
    row_contains = [False] * len(galaxies_map)
    column_contains = [False] * len(galaxies_map[0])
    
    
    for y in range(len(galaxies_map)):
        for x in range(len(galaxies_map[y])):
            if galaxies_map[y][x] == "#":
                galaxies.append((x, y))
                row_contains[y] = True
                column_contains[x] = True
    
    return galaxies, row_contains, column_contains
                


def get_distance(start, end, row_contains, column_contains):
    additional_size = 1000000 - 1
    x_min, y_min = start 
    x_max, y_max = end
    
    if x_max < x_min:
        x_max, x_min = x_min, x_max    
        
    if y_max < y_min:
        y_max, y_min = y_min, y_max  
        
    distance = x_max - x_min + y_max - y_min
    
    for i in range(x_min, x_max):
        if not column_contains[i]:
            distance += additional_size
            
    for i in range(y_min, y_max):
        if not row_contains[i]:
            distance += additional_size
    
    return distance
    
if __name__ == "__main__":
    test = False
    file = os.getcwd() + "/2023/inputs/" 
    if test:
        file += "test_input_11.txt"
    else:
        file += "input_11.txt"
        
    print(solve_map([[point for point in row] for row in open(file).read().split("\n")]))