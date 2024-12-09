with open("input.txt") as f:
    raw = f.read().strip()


def part1():
    id = 0
    blocks = []
    for i, num in enumerate(raw):
        if i % 2 == 0:
            blocks += [id] * int(num)
            id += 1
        else:
            blocks += [-1] * int(num)

    left = blocks.index(-1)
    for right in range(len(blocks) - 1, -1, -1):
        if right <= left:
            break
        if blocks[right] == -1:
            continue
        blocks[right], blocks[left] = blocks[left], blocks[right]
        left = blocks.index(-1)

    ans = 0
    for i, num in enumerate(blocks):
        if num != -1:
            ans += i * num

    return ans


def part2():
    blocks = []
    disk = []
    cur_start = 0
    id = 0
    for i, num in enumerate(raw):
        if i % 2 == 0:
            blocks.append([cur_start, cur_start + int(num) - 1, id])
            disk += [id] * int(num)
            cur_start += int(num)
            id += 1
        else:
            disk += [-1] * int(num)
            cur_start += int(num)

    for right in range(len(blocks) - 1, -1, -1):
        cap = 0
        space_needed = blocks[right][1] - blocks[right][0] + 1
        for z, slot in enumerate(disk):
            if z > blocks[right][0]:
                break
            if slot == -1:
                cap += 1
            else:
                cap = 0

            if cap == space_needed:
                for i in range(blocks[right][0], blocks[right][1] + 1):
                    disk[i] = -1

                for j in range(z, z - space_needed, -1):
                    disk[j] = blocks[right][2]
                break

    ans = 0
    for i, num in enumerate(disk):
        if num != -1:
            ans += i * num

    return ans


print(part2())
