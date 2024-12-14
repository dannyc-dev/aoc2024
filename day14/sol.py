with open("input.txt") as f:
    bots = f.read().split("\n")
    bots = [b.split() for b in bots if b.strip()]

bs = []
for bot in bots:
    numbers = [tuple(map(int, b.split("=")[1].split(","))) for b in bot]
    bs.append(numbers)

ROWS, COLS = 103, 101
# ROWS, COLS = 7, 11
ELAPSED = 100


def part1():
    mid_row = ROWS // 2
    mid_col = COLS // 2
    one, two, three, four = 0, 0, 0, 0

    def calc_section(r, c):
        nonlocal one, two, three, four
        if r < mid_row and c < mid_col:
            one += 1
        elif r < mid_row and c > mid_col:
            two += 1
        elif r > mid_row and c < mid_col:
            three += 1
        elif r > mid_row and c > mid_col:
            four += 1

    for (y, x), (vy, vx) in bs:
        nx, ny = (x + ELAPSED * vx) % ROWS, (y + vy * ELAPSED) % COLS
        calc_section(nx, ny)

    return one * two * three * four


# print(part1())


def part2():
    j = 0
    while j < 10000:
        grid = [[" "] * COLS for _ in range(ROWS)]
        for i, ((y, x), (vy, vx)) in enumerate(bs):
            nx, ny = (x + vx) % ROWS, (y + vy) % COLS
            bs[i][0] = [ny, nx]
            grid[nx][ny] = "#"

        print(f"Time: {j}")
        for row in grid:
            print("".join(str(x) for x in row))
        print("-" * 101)

        j += 1


part2()
