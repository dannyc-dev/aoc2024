with open('input.txt') as f:
    grid = f.read().split("\n")
    grid = [list(r) for r in grid if r.strip()]

ROWS, COLS = len(grid), len(grid[0])
dirs = {(1, 0), (0, 1), (-1, 0), (0, -1)}

def part1():
    def calc_perm(r, c, target) -> int:
        perm = 0
        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if (
                nr not in range(ROWS)
                or nc not in range(COLS)
                or grid[nr][nc] != target
            ):
                perm += 1
        return perm
    
    def dfs(r, c, target, island_cells):
        visited.add((r, c))
        island_cells.append((r, c))

        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if (
                nr in range(ROWS)
                and nc in range(COLS)
                and grid[nr][nc] == target
                and (nr, nc) not in visited
            ):
                dfs(nr, nc, target, island_cells)

    visited = set()
    ans = 0
    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) not in visited:
                island_cells = []
                dfs(row, col, grid[row][col], island_cells)

                if island_cells:
                    perm = 0
                    for r, c in island_cells:
                        perm += calc_perm(r, c, grid[row][col])
                
                    ans += len(island_cells) * perm
    return ans

def part2():
    dirs2 = [
        (-1, -1, (0, -1), (-1, 0)),
        (-1, 1, (0, 1), (-1, 0)), 
        (1, -1, (0, -1), (1, 0)), 
        (1, 1, (0, 1), (1, 0))
    ]
    def calc_sides(r, c, target) -> int:
        sides = 0
        for dr, dc, adj, adj1 in dirs2:
            diag_r, diag_c = dr + r, dc + c
            adj_r, adj_c = r + adj[0], c + adj[1]
            adj1_r, adj1_c = r + adj1[0], c + adj1[1]

            diag_out = diag_r not in range(ROWS) or diag_c not in range(COLS) or grid[diag_r][diag_c] != target
            adj_out = adj_r not in range(ROWS) or adj_c not in range(COLS) or grid[adj_r][adj_c] != target
            adj1_out = adj1_r not in range(ROWS) or adj1_c not in range(COLS) or grid[adj1_r][adj1_c] != target

            if diag_out and (adj_out and adj1_out):
                sides += 1
            if diag_out and not (adj_out or adj1_out):
                sides += 1
            if not diag_out and (adj_out and adj1_out):
                sides += 1

        return sides
        
    
    def dfs(r, c, target, island_cells):
        visited.add((r, c))
        island_cells.append((r, c))

        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if (
                nr in range(ROWS)
                and nc in range(COLS)
                and grid[nr][nc] == target
                and (nr, nc) not in visited
            ):
                dfs(nr, nc, target, island_cells)

    visited = set()
    ans = 0
    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) not in visited:
                island_cells = []
                dfs(row, col, grid[row][col], island_cells)

                if island_cells:
                    sides = 0
                    for r, c in island_cells:
                        sides += calc_sides(r, c, grid[row][col])
                
                    ans += len(island_cells) * sides
    return ans

print(part2())
