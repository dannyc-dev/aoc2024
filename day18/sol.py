import heapq

with open("input.txt") as f:
    pos = [list(map(int, r.split(","))) for r in f.read().split("\n") if r.strip()]

ROWS, COLS = 71, 71
DIRS = {(1, 0), (0, 1), (-1, 0), (0, -1)}


def build_grid(cur):
    grid = [["."] * ROWS for _ in range(COLS)]
    for i in range(cur):
        r, c = pos[i]
        grid[r][c] = "#"
    return grid


def print_grid(grid):
    for row in grid:
        print("".join(str(x) for x in row))


def part1():
    magic_number = 1024

    er, ec = ROWS - 1, COLS - 1
    grid = build_grid(magic_number)

    visited = set()
    q = [[0, 0, 0]]  # steps, row, col
    while q:
        step, row, col = heapq.heappop(q)

        if (row, col) == (er, ec):
            return step

        if (row, col) in visited:
            continue

        visited.add((row, col))
        for dr, dc in DIRS:
            nr, nc = dr + row, dc + col
            if (
                nr in range(ROWS)
                and nc in range(COLS)
                and (nr, nc) not in visited
                and grid[nr][nc] != "#"
            ):
                heapq.heappush(q, [step + 1, nr, nc])


# print(part1())


def part2():
    def bfs(grid):
        er, ec = ROWS - 1, COLS - 1
        visited = set()
        q = [[0, 0, 0]]  # steps, row, col
        while q:
            step, row, col = heapq.heappop(q)

            if (row, col) == (er, ec):
                return step

            if (row, col) in visited:
                continue

            visited.add((row, col))
            for dr, dc in DIRS:
                nr, nc = dr + row, dc + col
                if (
                    nr in range(ROWS)
                    and nc in range(COLS)
                    and (nr, nc) not in visited
                    and grid[nr][nc] != "#"
                ):
                    heapq.heappush(q, [step + 1, nr, nc])

    left, right = 0, len(pos)

    while left < right:
        mid = (left + right) // 2
        grid = build_grid(mid)

        if bfs(grid):
            left = mid + 1
        else:
            right = mid

    if not bfs(build_grid(left)):
        return pos[left - 1]

    return pos[left]


print(part2())
