from collections import Counter
with open("input.txt") as data_file:
    nums = data_file.read().split("\n")
    nums = [line for line in nums if line.strip()]

left, right = [], []
for line in nums:
    line_nums = line.split()
    left.append(int(line_nums[0]))
    right.append(int(line_nums[1]))

def part1():
    left.sort()
    right.sort()

    total = 0
    for left_num, right_num in zip(left, right):
        dist = abs(int(left_num) - int(right_num))
        total += dist

    return total

def part2():
    right_counter = Counter(right)
    total = 0


    total = 0
    for num in left:
        total += num * right_counter[num]

    return total

print(part1())
print(part2())
