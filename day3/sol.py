import re

with open("input.txt") as f:
    text = f.read()


def part1():
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(pattern, text)
    ans = 0
    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        ans += x * y
    return ans


def part2():
    pattern = r"(?P<do>do(?!n't))|(?P<dont>don't)|(?P<mul>mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\))"

    matches = re.finditer(pattern, text)
    skip = False
    ans = 0
    for match in matches:
        if match.group("dont"):
            skip = True
        elif match.group("do"):
            skip = False
        else:
            if skip:
                continue
            else:
                x, y = int(match.group("x")), int(match.group("y"))
                ans += x * y
    return ans


print(part2())
