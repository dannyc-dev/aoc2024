with open('input.txt') as f:
    bots = f.read().split("\n")
    bots = [b.split() for b in bots if b.strip()]

bs = []
for bot in bots:
    numbers = [tuple(map(int, b.split('=')[1].split(','))) for b in bot]
    bs.append(numbers)

ROWS, COLS = 103, 101
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
    pass


    
