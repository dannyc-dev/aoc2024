with open('input.txt') as file:
    levels = file.read().split("\n")
    levels = levels[:-1]

levels = [[int(x) for x in l.split(" ")] for l in levels]

def check_equal(level):
    if len(level) == len(set(level)):
        return True
    return False

def check_increasing(level):
    if level[0] < level[1]:
        return True
    else:
        return False
    
def part1():
    count = 0
    for level in levels:
        if check_equal(level):
            if check_increasing(level):
                prev = 0
                for i in range(1, len(level)):
                    if level[prev] < level[i] and level[prev] + 3 >= level[i]:
                        prev = i
                    else:
                        break
                else:
                    count += 1
            else:
                prev = 0
                for i in range(1, len(level)):
                    if level[prev] > level[i] and level[prev] - 3 <= level[i]:
                        prev = i
                    else:
                        break
                else:
                    count += 1
    return count 

# print(part1()) 

def dp_increasing(level):
    prev = 0
    for i in range(1, len(level)):
        if level[prev] < level[i] and level[prev] + 3 >= level[i]:
            prev = i
        else:
            break
    else:
        return True

    return False

def dp_decreasing(level):
    prev = 0
    for i in range(1, len(level)):
        if level[prev] > level[i] and level[prev] - 3 <= level[i]:
            prev = i
        else:
            break
    else:
        return True
    
def part2():
    count = 0
    for level in levels:
        if not dp_increasing(level):
            for i in range(len(level)):
                if dp_increasing(level[:i] + level[i + 1:]):
                    count += 1
                    break
        else:
            count += 1
        if not dp_decreasing(level):
            for i in range(len(level)):
                if dp_decreasing(level[:i] + level[i + 1:]):
                    count += 1
                    break
        else:
            count += 1
    return count

print(part2())
            
    
    
