from functools import cache
import sys

with open('input.txt') as file:
    grid = file.read().split("\n")
    grid = [list(row) for row in grid if row.strip()]

ROWS, COLS = len(grid), len(grid[0])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()

def find_start():
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "^":
                return (row, col)

start = find_start()
sys.setrecursionlimit(99999)
def part1():
    @cache
    def dfs(row, col, dir):
        nr, nc = row + dirs[dir % 4][0], col + dirs[dir % 4][1]

        if (nr not in range(ROWS) or nc not in range(COLS)):
            return
        
        if grid[nr][nc] == "#":
            dfs(row, col, dir + 1)
        else:
            visited.add((nr, nc))
            dfs(nr, nc, dir)

    dfs(start[0], start[1], 0)
    return len(visited)

def part2():
    part1()
    original_path = visited.copy()
    
    def check_for_loop(block_pos):
        pos_vectors = set()
        row, col = start
        dir = 0
        
        while True:
            state = (row, col, dir % 4)
            if state in pos_vectors:
                return True
            pos_vectors.add(state)
            
            nr, nc = row + dirs[dir % 4][0], col + dirs[dir % 4][1]
            
            if not (0 <= nr < ROWS and 0 <= nc < COLS):
                return False
                
            if grid[nr][nc] == "#" or (nr, nc) == block_pos:
                dir += 1
            else:
                row, col = nr, nc
    
    count = 0
    for pos in original_path - {(start[0], start[1])}:
        if check_for_loop(pos):
            count += 1
    
    return count

print(part2())
