with open("input.txt") as file:
    grid = file.read().split("\n")
    grid = [list(r) for row in grid for r in row.split() if row.strip()]


def part1():
    dirs = {(0, 1), (1, 1), (-1, 1), (1, -1), (1, 0), (-1, -1), (-1, 0), (0, -1)}

    ROWS, COLS = len(grid), len(grid[0])
    target = "XMAS"

    def dfs(r, c, i, dir):
        if i == 4:
            return 1

        count = 0
        if dir is None:
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if (
                    nr in range(ROWS)
                    and nc in range(COLS)
                    and grid[nr][nc] == target[i]
                ):
                    count += dfs(nr, nc, i + 1, (dr, dc))
        else:
            nr, nc = r + dir[0], c + dir[1]
            if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == target[i]:
                count += dfs(nr, nc, i + 1, dir)

        return count

    count = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "X":
                count += dfs(row, col, 1, None)

    return count


# print(part1())


def part2():
    target = "MAS"
    ROWS, COLS = len(grid), len(grid[0])
    dirs = {(1, 1), (1, -1), (-1, -1), (-1, 1)}

    def dfs(r, c, i, dir):
        if i == 3:
            return True

        nr, nc = r + dir[0], c + dir[1]
        if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == target[i]:
            if dfs(nr, nc, i + 1, dir):
                return True
        return False

    count = 0
    mids = set()
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "M":
                for dr, dc in dirs:
                    if dfs(row, col, 1, (dr, dc)):
                        mid_r, mid_c = row + dr, col + dc
                        missing = {"M", "S"}
                        for cr, cc in dirs - {(dr, dc)}:
                            if not missing:
                                break
                            nr, nc = cr + mid_r, cc + mid_c
                            if nr == row and nc == col:
                                continue
                            if grid[nr][nc] == "M":
                                missing.discard("M")
                            elif grid[nr][nc] == "S":
                                missing.discard("S")

                        if not missing:
                            count += 1
                            mids.add((mid_r, mid_c))

    return len(mids)


print(part2())
