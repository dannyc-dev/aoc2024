from collections import defaultdict


with open("input.txt") as f:
    stones = f.read().split()
    stones = [int(n) for n in stones]


def part1(stones):
    cache = {}

    def calc(stones):
        out = []
        if tuple(stones) in cache:
            return cache[tuple(stones)]

        for num in stones:
            if num == 0:
                out.append(1)
            elif len(str(num)) % 2 == 0:
                half = len(str(num)) // 2
                left, right = (
                    int(str(num)[:half]),
                    int(str(num)[half:]),
                )
                out.append(left)
                out.append(right)
            else:
                out.append(num * 2024)

        cache[tuple(stones)] = out
        return out

    for _ in range(25):
        stones = calc(stones)

    return len(stones)


# print(part1(stones))


def part2(stones):
    cache = defaultdict(int)

    for stone in stones:
        cache[stone] += 1

    def calc(stones):
        out = defaultdict(int)

        for stone, num in stones.items():
            if stone == 0:
                out[1] += num
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                left, right = (
                    int(str(stone)[:half]),
                    int(str(stone)[half:]),
                )
                out[left] += num
                out[right] += num
            else:
                out[stone * 2024] += num

        return out

    for _ in range(75):
        cache = calc(cache)

    return sum(cache.values())


print(part2(stones))
