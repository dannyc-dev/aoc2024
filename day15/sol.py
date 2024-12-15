from typing import List

with open('input.txt') as f:
    grid, ins = f.read().split("\n\n") 
    
grid: List[List[str]] = [list(r) for r in grid.split("\n")]
ins = [str(r) for r in ins if r.strip()]
ins = "".join(ins)

dirs = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}

def get_start(grid):
    start = (0, 0)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                return (row, col)

    return start

def print_grid(grid):
    for row in grid:
        print("".join(str(x) for x in row))


def part1():
    ROWS, COLS = len(grid), len(grid[0])
    r, c = get_start(grid)

    def calc_last_box(r, c, dir):
        og_r, og_c = r, c
        while grid[r + dir[0]][c + dir[1]] == "O":
            r, c = r + dir[0], c + dir[1]

        if grid[r + dir[0]][c + dir[1]] == "#":
            return False
        
        grid[og_r][og_c] = "."
        grid[r + dir[0]][c + dir[1]] = "O"
        grid[og_r + dir[0]][og_c + dir[1]] = "@"
        return True 


    for move in ins:
        # print(f"Cur pos: {r, c}")
        # print(f"Move: {move}")
        # print("Current board:")
        # print_grid(grid)

        nr, nc = dirs[move][0] + r, dirs[move][1] + c
        if grid[nr][nc] == "#":
            continue

        if grid[nr][nc] == ".":
            grid[r][c] = "."
            grid[nr][nc] = "@"
            r, c = nr, nc
            # print_grid(grid)
            continue

        if grid[nr][nc] == "O":
            if calc_last_box(r, c, dirs[move]):
                r, c = nr, nc

        # print_grid(grid)

    score = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "O":
                score += 100 * row + col

    return score

# print(part1())

def transform_grid(grid):
    new_grid = []
    for row in range(len(grid)):
        new_row = []
        for col in range(len(grid[0])):
            if grid[row][col] == ".":
                new_row.append(".")
                new_row.append(".")
            elif grid[row][col] == "@":
                new_row.append("@")
                new_row.append(".")
            elif grid[row][col] == "#":
                new_row.append("#")
                new_row.append("#")
            else:
                new_row.append("[")
                new_row.append("]")
        new_grid.append(new_row)

    return new_grid

def part2(grid):

    r, c = get_start(grid)

    def calc_y_box(r, c, dir, box_group):
        if grid[r][c] == "[":
            open = [r, c]
            close = [r, c + 1]
        else:
            open = [r, c - 1]
            close = [r, c]

        if grid[open[0] + dir[0]][open[1] + dir[1]] == "#" or grid[close[0] + dir[0]][close[1] + dir[1]] == "#":
            return False

        box_group.append(open)
        
        for row, col in [open, close]:
            nr, nc = row + dir[0], col + dir[1]
            if grid[nr][nc] in {"[", "]"}:
                if not calc_y_box(nr, nc, dir, box_group):
                    return False

        return box_group

    def move_boxes(boxes, dir):
        if dir[0] == -1: 
            for r, c in sorted(boxes):
                nr, nc = r + dir[0], c + dir[1]
                nrc, ncc = r + dir[0], c + 1 + dir[1]
                grid[nr][nc], grid[nrc][ncc] = "[", "]"
                grid[r][c], grid[r][c + 1] = ".", "."
        else:
            for r, c in sorted(boxes, reverse=True):
                nr, nc = r + dir[0], c + dir[1]
                nrc, ncc = r + dir[0], c + 1 + dir[1]
                grid[nr][nc], grid[nrc][ncc] = "[", "]"
                grid[r][c], grid[r][c + 1] = ".", "."
 

    def calc_x_box(r, c, dir):
        og_c = c
        while grid[r + dir[0]][c + dir[1]] in {"[", "]"}:
            r, c = r + dir[0], c + dir[1]

        if grid[r + dir[0]][c + dir[1]] == "#":
            return False

        nc = c + dir[1]
        op_y = dir[1] * -1
        while nc != og_c:
            grid[r][nc], grid[r][c] = grid[r][c], grid[r][nc]
            nc += op_y
            c += op_y

        return (r, nc + dir[1])

    for move in ins:
        # print(f"Cur pos: {r, c}")
        # print(f"Move: {move}")
        # print("Current board:")
        # print_grid(new_grid)
        
        nr, nc = dirs[move][0] + r, dirs[move][1] + c
        if grid[nr][nc] == "#":
            continue

        if grid[nr][nc] == ".":
            grid[r][c] = "."
            grid[nr][nc] = "@"
            r, c = nr, nc
            # print_grid(grid)
            continue

        if grid[nr][nc] in {"[", "]"}:
            if move in {">", "<"}:
                if new_pos := calc_x_box(r, c, dirs[move]):
                    r, c = new_pos[0], new_pos[1]
            else:
                boxes_to_push = calc_y_box(nr, nc, dirs[move], [])
                if boxes_to_push:
                    move_boxes(boxes_to_push, dirs[move])
                    grid[r][c] = "."
                    grid[nr][nc] = "@"
                    r, c = nr, nc
        # print_grid(grid)

    
    print_grid(grid)
    score = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "[":
                score += 100 * row + col

    return score

new_grid = transform_grid(grid)
print(part2(new_grid))



