with open("input.txt") as f:
    grid = f.read().split("\n")
    grid = [list(map(int, row)) for row in grid if row.strip()]

ROWS, COLS = len(grid), len(grid[0])
dirs = {(1, 0), (0, 1), (-1, 0), (0, -1)}


def part1():
    def dfs(r, c, target, seen):
        if grid[r][c] == 9:
            if (r, c) not in seen:
                seen.add((r, c))
                return 1
            else:
                return 0

        ans = 0
        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == target:
                ans += dfs(nr, nc, target + 1, seen)

        return ans

    count = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 0:
                count += dfs(row, col, 1, set())
    return count


print(part1())


def part2():
    def dfs(r, c, target):
        if grid[r][c] == 9:
            return 1

        ans = 0
        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == target:
                ans += dfs(nr, nc, target + 1)

        return ans

    count = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 0:
                count += dfs(row, col, 1)
    return count


print(part2())
