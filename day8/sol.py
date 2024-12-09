from collections import defaultdict

with open('input.txt') as f:
    grid = f.read().split("\n")
    grid = [list(r) for r in grid if r.strip()]

ROWS, COLS = len(grid), len(grid[0])
nodes = defaultdict(list)
antinodes = set()
def part1():
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] != ".":
                nodes[grid[r][c]].append((r, c))

    for node, pos in nodes.items():
        for i in range(len(pos) - 1):
            for j in range(i + 1, len(pos)):
                x_dist, y_dist = pos[i][0] - pos[j][0], pos[i][1] - pos[j][1]
                nix, niy = pos[i][0] + x_dist, pos[i][1] + y_dist
                njx, njy = pos[j][0] - x_dist, pos[j][1] - y_dist
                if nix in range(ROWS) and niy in range(COLS):
                    antinodes.add((nix, niy))
                if njx in range(ROWS) and njy in range(COLS):
                    antinodes.add((njx, njy))

    print(len(antinodes))

part2_antinodes = set()
def part2():
    for node, pos in nodes.items():
        for i in range(len(pos) - 1):
            for j in range(i + 1, len(pos)):
                x_dist, y_dist = pos[i][0] - pos[j][0], pos[i][1] - pos[j][1]
                nix, niy = pos[i][0] + x_dist, pos[i][1] + y_dist
                njx, njy = pos[j][0] - x_dist, pos[j][1] - y_dist
                i_count, j_count = 0, 0
                while nix in range(ROWS) and niy in range(COLS):
                    i_count += 1
                    part2_antinodes.add((nix, niy))
                    nix, niy = nix + x_dist, niy + y_dist

                part2_antinodes.add((pos[i][0], pos[i][1]))
                part2_antinodes.add((pos[j][0], pos[j][1]))

                while njx in range(ROWS) and njy in range(COLS):
                    j_count += 1
                    part2_antinodes.add((njx, njy))
                    njx, njy = njx - x_dist, njy - y_dist
                
                part2_antinodes.add((pos[i][0], pos[i][1]))
                part2_antinodes.add((pos[j][0], pos[j][1]))
                

    print(len(part2_antinodes))
                    

print(part1())
print(part2())
# 2, 5
# 3, 7
#
# 1, 2
#
# 1, 3
# 4, 9
