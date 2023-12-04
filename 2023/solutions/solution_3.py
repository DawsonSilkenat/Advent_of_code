import os 

test_answer = 4361
filename = os.getcwd() + "/2023/inputs/" + "input_3.txt"


def get_boundrys(x, y, grid):
    left = x
    while left >= 0 and grid[y][left - 1].isdigit():
        left -= 1
    right = x 
    while right < len(grid[y]) - 1 and grid[y][right + 1].isdigit():
        right += 1
  
    return left, right

def check_for_symbol(x, y, grid):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return False
    return not (grid[y][x].isdigit() or grid[y][x] == '.')
    
def boarder_contains_symbol(left, right, y, grid):
    for i in [y - 1, y, y + 1]:
        for j in range(left - 1, right + 2):
            if check_for_symbol(j, i, grid):
                return True
    return False


if __name__ == "__main__":
    grid = [[sym for sym in row if sym != "\n"] for row in open(filename)]
    total = 0
    for y in range(len(grid)):
        x = 0 
        while x < len(grid[y]):
            if grid[y][x].isdigit():
                left, right = get_boundrys(x, y, grid)
                if boarder_contains_symbol(left, right, y, grid):
                    total += int("".join(grid[y][left:right + 1]))
                x = right + 1
            else: 
                x += 1
    print(total)