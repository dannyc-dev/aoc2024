import heapq
from itertools import product


with open("test.txt") as f:
    code = f.read().split("\n")
    codes = [c for c in code if c.strip()]

num_grid = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]
dir_grid = [["#", "^", "A"], ["<", "v", ">"]]

dir_trans = {(1, 0): "v", (-1, 0): "^", (0, 1): ">", (0, -1): "<"}
DIRS = {(1, 0), (-1, 0), (0, 1), (0, -1)}

def part1():
    def bfs(r, c, grid, target):
        q = [[0, 0, r, c, ""]] # step, idx, row, col, path
        min_step = None
        ans = []
        ROWS, COLS = len(grid), len(grid[0])
        while q:
            step, idx, r, c, path = heapq.heappop(q) 

            if min_step is not None and step > min_step:
                return ans

            if -idx == len(target):
                min_step = step
                ans.append(path)
                continue

            if grid[r][c] == target[-idx]:
                heapq.heappush(q, [step + 1, idx - 1, r, c, path + "A"])
                continue
            
            for dr, dc in DIRS:
                nr, nc = dr + r, dc + c
                if (
                    nr in range(ROWS)
                    and nc in range(COLS)
                    and grid[nr][nc] != "#"
                ):
                    move = dir_trans[(dr, dc)]
                    if target[-idx] == grid[nr][nc]:
                        heapq.heappush(q, [step + 1, idx - 1, nr, nc, path + move + "A"])
                    else:
                        heapq.heappush(q, [step + 1, idx, nr, nc, path + move])
        return ans  
    
    def split_chunks(path):
        chunks = []
        current = ""
        i = 0
        while i < len(path):
            current += path[i]
            if path[i] == 'A':
                chunks.append(current)
                current = ""
                while i + 1 < len(path) and path[i + 1] == 'A':
                    chunks.append('A')
                    i += 1
            i += 1
            
        if current:
            chunks.append(current)
            
        return chunks
    
    cache = {}
    total = 0
    for code in codes:
        paths = bfs(3, 2, num_grid, code)
        shortest_code = float('inf')
        for path in paths:
            possible_paths = []
            for chunk in split_chunks(path):
                if chunk in cache:
                    possible_paths.append(cache[chunk])
                else:
                    p = bfs(0, 2, dir_grid, chunk)
                    possible_paths.append(p)

             
            possible = list(product(*possible_paths))
            combined_strings = [''.join(combo) for combo in possible]
            
            for path in combined_strings:
                possible_final = []
                for chunk in split_chunks(path):
                    if chunk in cache:
                        possible_final.append(cache[chunk])
                    else:
                        p = bfs(0, 2, dir_grid, chunk)
                        possible_final.append(p)
            
                # print(possible_final)
                # final = list(product(*possible_final))
                # combined_final = [''.join(combo) for combo in final]
                shortest = min(product(*possible_final), key=lambda x: sum(len(s) for s in x))
                shortest_code = min(shortest_code, len(''.join(shortest)))
            
        num = ""
        for char in code:
            if char.isdigit():
                num += char
        num = int(num)
        total += num * shortest_code
            
                
    print(total)
 
# print(part1())

