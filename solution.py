
def gridChallenge(grid):
    new_grid = []
    
    for str in grid:
        sorted_list = sorted(str)
        new_str = ''.join(sorted_list)
        new_grid.append(new_str)
    
    row = 0
    col = 0
    
    total = 0
    
    while col < len(new_grid[0]):
        count = 0
        for row in range(len(new_grid)-1):
            if new_grid[row][col] <= new_grid[row+1][col]:
                count += 1
        if count == len(new_grid)-1:
            total += 1
        col += 1
    
    if total == len(new_grid[0]):
        return 'YES'
    else:
        return 'NO'
