import os



def get_connections(grid, coord):
    x, y = coord
    
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return []
    
    north = (x, y - 1)
    south = (x, y + 1)
    east = (x + 1, y)
    west = (x - 1, y)
    
    tile = grid[y][x]
    
    match tile:
        case "|":
            return [north, south]
        case "-":
            return [east, west]
        case "L":
            return [north, east]
        case "J":
            return [north, west]
        case "7":
            return [south, west]
        case "F":
            return [south, east]
        case "S":
            return [north, south, east, west]
        
    return []


def find_path(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                start = (x, y)
    
    path = []
    
    for next in get_connections(grid, start):
        connections = get_connections(grid, next)
        if start in connections:
            path.append(next) 
            connections.remove(start)
            path += connections
            break
    
    while path[-1] != start:
        connections = get_connections(grid, path[-1])
        connections.remove(path[-2])
        path += connections
    
    return path


def fill_grid_empty(grid, path):
    # Mostly for looking at what the actual path looks like
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x,y) not in path:
                grid[y][x] = "."   


def add_space_between(grid, path):
    spacer = "E"
    blocker = "B"
    grid_with_spacers = []
    fill_grid_empty(grid, path)
    
    for row in grid:
        grid_with_spacers.append([spacer] * (2 * len(row) + 1))
        spacer_row = []
        for tile in row:
            spacer_row.append(spacer)
            spacer_row.append(tile)
        spacer_row.append(spacer)
        grid_with_spacers.append(spacer_row)
    grid_with_spacers.append([spacer] * (2 * len(row) + 1))
    
    
    for coord in path[:-1]:
        spaced_x = 2 * coord[0] + 1
        spaced_y = 2 * coord[1] + 1
        
        for (x, y) in get_connections(grid_with_spacers, (spaced_x, spaced_y)):
            grid_with_spacers[y][x] = blocker

    return grid_with_spacers

def flood_fill(grid, start=(0,0)):
    queue = [start] 
    
    while queue:
        x, y = queue.pop(0)
        if not (y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y])) and (grid[y][x] == "." or grid[y][x] == "E"):
            grid[y][x] = "O"
            queue += [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        
    return grid
        
        

if __name__ == "__main__":
    test = False
    file = os.getcwd() + "/2023/inputs/" 
    if test:
        file += "test_input_10.txt"
    else:
        file += "input_10.txt"
    
    grid = [[tile for tile in row] for row in open(file).read().split("\n")]
    path = find_path(grid)
    
    count = 0
    for row in flood_fill(add_space_between(grid, path)):
        for tile in row:
            if tile == ".":
                count += 1
    
    print(count)
    