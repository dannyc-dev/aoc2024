import heapq

with open("input.txt") as f:
    grid = f.read().split("\n")
    grid = [list(r) for r in grid if r.split()]

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


def part1():
    r, c = find_start()
    re, ce = find_end()
    assert r != 0 and c != 0
    assert re != 0 and ce != 0

    def get_turn_cost(cur_dir, tar_dir):
        if cur_dir == tar_dir:
            return 0

        diff = abs(tar_dir - cur_dir)

        if diff == 2:
            return 2000

        return 1000

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    q = [(0, r, c, 1, [])]  # score, row, col, direction
    visited = set()
    total_scores = {}

    while q:
        score, r, c, dir, path = heapq.heappop(q)

        if (r, c) == (re, ce):
            return score, path, total_scores

        if (r, c, dir) in visited:
            continue

        total_scores[(r, c, dir)] = score
        visited.add((r, c, dir))
        for i, (dr, dc) in enumerate(dirs):
            nr, nc = dr + r, dc + c
            if (
                nr in range(ROWS)
                and nc in range(COLS)
                and (nr, nc, i) not in visited
                and grid[nr][nc] != "#"
            ):
                cost = get_turn_cost(dir, i)
                new_path = path.copy()
                new_path.append((nr, nc, i))
                heapq.heappush(q, [score + cost + 1, nr, nc, i, new_path])


# print(part1())


def part2(target_score, target_path, total_scores):
    r, c = find_start()
    re, ce = find_end()
    assert r != 0 and c != 0
    assert re != 0 and ce != 0

    def get_turn_cost(cur_dir, tar_dir):
        if cur_dir == tar_dir:
            return 0

        diff = abs(tar_dir - cur_dir)

        if diff == 2:
            return 2000

        return 1000

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    q = [[0, r, c, 1, set([(r, c)])]]  # score, row, col, direction, path
    paths = set([(r, c) for r, c, _ in target_path])

    to_delete = []
    for r, c, d in total_scores:
        if (r, c, d) not in target_path:
            to_delete.append((r, c, d))

    for r, c, d in to_delete:
        del total_scores[(r, c, d)]

    visited = set()
    while q:
        score, r, c, dir, path = heapq.heappop(q)

        if score > target_score:
            break

        if (r, c) == (re, ce) and score == target_score:
            paths |= path

        if (r, c, dir) in target_path and (r, c, dir) in total_scores:
            if total_scores[(r, c, dir)] >= score:
                paths |= path
            else:
                continue

        visited.add((r, c, dir))

        for i, (dr, dc) in enumerate(dirs):
            if (dr, dc) == (-dirs[dir][0], -dirs[dir][1]):
                continue
            nr, nc = dr + r, dc + c
            if (
                nr in range(ROWS)
                and nc in range(COLS)
                and grid[nr][nc] != "#"
                and (nr, nc, i) not in visited
            ):
                cost = get_turn_cost(dir, i)
                heapq.heappush(q, [score + cost + 1, nr, nc, i, path | set([(nr, nc)])])

    return len(paths)


target_score, path, total_scores = part1()
print(part2(target_score, path, total_scores))
