import heapq
from collections import defaultdict

with open("input.txt") as f:
    grid = f.read().split("\n")
    grid = [list(r) for r in grid if r.strip()]


def print_grid(grid):
    for row in grid:
        print("".join(str(x) for x in row))


ROWS, COLS = len(grid), len(grid[0])


def find_start():
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "S":
                return (row, col)
    return (0, 0)


def find_end():
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "E":
                return (row, col)
    return (0, 0)


DIRS = {(1, 0), (0, 1), (-1, 0), (0, -1)}


def part1(start, end):
    def bfs(r, c, re, ce):
        q = [[0, r, c, []]]  # steps, row, col, path
        visited = set()
        while q:
            step, r, c, path = heapq.heappop(q)

            if (r, c) == (re, ce):
                return path, step

            visited.add((r, c))
            for dr, dc in DIRS:
                nr, nc = dr + r, dc + c
                if (
                    nr in range(ROWS)
                    and nc in range(COLS)
                    and (nr, nc) not in visited
                    and grid[nr][nc] != "#"
                ):
                    heapq.heappush(q, [step + 1, nr, nc, path + [[nr, nc]]])

    path, total = bfs(start[0], start[1], end[0], end[1])
    path_dict = {}
    for i, (r, c) in enumerate(path):
        path_dict[(r, c)] = i

    cheats = defaultdict(int)

    for i, (r, c) in enumerate(path):
        for dr, dc in DIRS:
            nr, nc = dr + r, dc + c
            if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == "#":
                for tr, tc in DIRS:
                    if (tr, tc) == (-dr, -dc):
                        continue
                    sr, sc = tr + nr, tc + nc
                    if (
                        sr in range(ROWS)
                        and sc in range(COLS)
                        and (sr, sc) in path_dict
                    ):
                        edx = path_dict[(sr, sc)]
                        if edx > i:
                            pico_save = edx - i - 2
                            cheats[pico_save] += 1

    total = 0
    for pico_saved, count in cheats.items():
        if pico_saved >= 100:
            total += count

    return total


def part2(start, end):
    def bfs(r, c, re, ce):
        q = [[0, r, c, [[r, c]]]]  # steps, row, col, path
        visited = set()
        while q:
            step, r, c, path = heapq.heappop(q)

            if (r, c) == (re, ce):
                return path, step

            visited.add((r, c))
            for dr, dc in DIRS:
                nr, nc = dr + r, dc + c
                if (
                    nr in range(ROWS)
                    and nc in range(COLS)
                    and (nr, nc) not in visited
                    and grid[nr][nc] != "#"
                ):
                    heapq.heappush(q, [step + 1, nr, nc, path + [[nr, nc]]])

    def calc_pico_saved(r, c, row, col, idx):
        if r in range(ROWS) and c in range(COLS) and (r, c) in path_dict:
            edx = path_dict[(r, c)]
            pico_saved = edx - idx - (abs(row - r) + abs(col - c))
            if pico_saved > 0:
                cheats[pico_saved] += 1

    def calc_shortcut(row, col, idx, distance=20):
        for dx in range(-distance, distance + 1):
            remaining_steps = distance - abs(dx)
            for dy in range(-remaining_steps, remaining_steps + 1):
                calc_pico_saved(row + dy, col + dx, row, col, idx)

    path, total = bfs(start[0], start[1], end[0], end[1])
    path_dict = {}
    for i, (r, c) in enumerate(path):
        path_dict[(r, c)] = i

    cheats = defaultdict(int)
    for sdx, (r, c) in enumerate(path):
        calc_shortcut(r, c, sdx)

    total = 0
    for pico_saved, count in cheats.items():
        if pico_saved >= 100:
            total += count

    return total


start = find_start()
end = find_end()
print(part2(start, end))
