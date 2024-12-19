from functools import cache

with open("input.txt") as f:
    pats, targets = f.read().split("\n\n")
    pats = [p.strip() for p in pats.split(",")]
    targets = [t for t in targets.split("\n") if t.strip()]


def part1():
    def dp(target):
        if not target:
            return True

        for pattern in pats:
            pattern_len = len(pattern)
            if target[:pattern_len] == pattern:
                if dp(target[pattern_len:]):
                    return True

        return False

    count = 0
    for target in targets:
        if dp(target):
            count += 1

    return count


def part2():
    @cache
    def dp(target):
        if not target:
            return 1

        count = 0
        for pattern in pats:
            pattern_len = len(pattern)
            if target[:pattern_len] == pattern:
                count += dp(target[pattern_len:])

        return count

    count = 0
    for target in targets:
        if total := dp(target):
            count += total

    return count


print(part2())
