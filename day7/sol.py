with open('input.txt') as f:
    eqs = f.read().split("\n")
    eqs = [row.split(":") for row in eqs]

input = []
for eq in eqs:
    if eq[0]:
        row = list(map(int, eq[1].strip().split(" ")))
        input.append([int(eq[0]), row])

def part1():

    def dp(i, possible, total, target):
        if total == target and i >= len(possible):
            return True

        if i >= len(possible):
            return False

        if total > target:
            return False

        # add 
        if dp(i + 1, possible, total + possible[i], target):
            return True

        # mul
        if dp(i + 1, possible, total * possible[i], target):
            return True

        return False
    
    total = 0
    for target, possible in input:
        if dp(0, possible, 0, target):
            total += target
    return total


def part2():
    
    def dp(i, possible, total, target):
        if total == target and i >= len(possible):
            return True

        if i >= len(possible):
            return False

        if total > target:
            return False

        # add 
        if dp(i + 1, possible, total + possible[i], target):
            return True

        # mul
        if dp(i + 1, possible, total * possible[i], target):
            return True

        # concat
        if i > 0:
            if dp(i + 1, possible, int(str(total) + str(possible[i])), target):
                return True

        return False
    
    total = 0
    for target, possible in input:
        if dp(0, possible, 0, target):
            total += target
    return total

print(part1())
print(part2())
