import os 

test_answer = 4361
filename = os.getcwd() + "/2023/inputs/" + "input_3.txt"


def get_boundrys(x, y, grid):
    if not grid[y][x].isdigit():
        return None

    left = x
    while left >= 0 and grid[y][left - 1].isdigit():
        left -= 1
    right = x 
    while right < len(grid[y]) - 1 and grid[y][right + 1].isdigit():
        right += 1
  
    return y, left, right

def check_for_digit(x, y, grid):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return False
    return grid[y][x].isdigit()
    
def get_gear_ratio(x, y, grid):
    nums = []
    for i in [y - 1, y, y + 1]:
        for j in [x - 1, x, x + 1]:
            if check_for_digit(j, i, grid):
                bounds = get_boundrys(j, i, grid)
                if not bounds in nums: 
                    nums.append(bounds)
                    
    if len(nums) > 1:
        ratio = 1 
        for num in nums:
            ratio *= int("".join(grid[num[0]][num[1] : num[2] + 1]))
        return ratio
        
    return 0


if __name__ == "__main__":
    grid = [[sym for sym in row if sym != "\n"] for row in open(filename)]
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "*":
                total += get_gear_ratio(x, y, grid)
            
    print(total)