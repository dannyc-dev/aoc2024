with open("input.txt") as f:
    machines = f.read().split("\n\n")
    machines = [machine.strip().split("\n") for machine in machines]

import re
from functools import cache


def part1():
    @cache
    def dp(ax, ay, bx, by, px, py, a_presses, b_presses):
        if px == 0 and py == 0:
            return a_presses * 3 + b_presses

        if a_presses > 100 or b_presses > 100:
            return float("inf")

        if px < 0 or py < 0:
            return float("inf")

        press_a = dp(ax, ay, bx, by, px - ax, py - ay, a_presses + 1, b_presses)
        press_b = dp(ax, ay, bx, by, px - bx, py - by, a_presses, b_presses + 1)

        return min(press_a, press_b)

    ans = 0
    for machine in machines:
        vars = []
        for i in range(3):
            if i < 2:
                nums = re.findall(r"\+(\d+)", machine[i])
                vars += nums
            else:
                nums = re.findall(r"\=(\d+)", machine[i])
                vars += nums

        min_tokens = dp(
            int(vars[0]),
            int(vars[1]),
            int(vars[2]),
            int(vars[3]),
            int(vars[4]),
            int(vars[5]),
            0,
            0,
        )

        if min_tokens != float("inf"):
            ans += min_tokens

    return ans


# print(part1())


def part2():
   
    def calc_prize(ax, ay, bx, by, px, py):
        a_presses = ((px * by) - (py * bx)) / ((ax * by) - (ay * bx))
        b_presses = (px - ax * a_presses) / bx

        if a_presses % 1 == 0 and b_presses % 1 == 0:
            return int(a_presses * 3 + b_presses)

        return 0
    
    ans = 0
    for machine in machines:
        vars = []
        for i in range(3):
            if i < 2:
                nums = re.findall(r"\+(\d+)", machine[i])
                vars += nums
            else:
                nums = re.findall(r"\=(\d+)", machine[i])
                vars += nums

        min_tokens = calc_prize(
            int(vars[0]),
            int(vars[1]),
            int(vars[2]),
            int(vars[3]),
            int(vars[4]) + 10000000000000,
            int(vars[5]) + 10000000000000,
        )

        ans += min_tokens

    return ans

print(part2())
