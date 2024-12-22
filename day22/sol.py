from functools import cache
from collections import defaultdict, deque

with open('input.txt') as f:
    nums = f.read().split("\n")
    nums = [num for num in nums if num.strip()]

def part1():
   
    @cache
    def mix(secret_num, num):
        return secret_num ^ num

    @cache
    def prune(secret_num):
        return secret_num % 16777216

    @cache
    def calc(num):
        mixer = num * 64
        num = mix(num, mixer)
        num = prune(num)
        
        mixer2 = num // 32
        num = mix(num, mixer2)
        num = prune(num)

        mixer3 = num * 2048
        num = mix(num, mixer3)
        num = prune(num)

        return num

    total = 0 
    for num in nums:
        num = int(num)
        # tmp = num
        for _ in range(2000):
            num = calc(num)
        # print(f"{tmp}: {num}")
        total += num

    return total

# print(part1())

def part2():
    @cache
    def mix(secret_num, num):
        return secret_num ^ num

    @cache
    def prune(secret_num):
        return secret_num % 16777216

    @cache
    def calc(num):
        mixer = num * 64
        num = mix(num, mixer)
        num = prune(num)
        
        mixer2 = num // 32
        num = mix(num, mixer2)
        num = prune(num)

        mixer3 = num * 2048
        num = mix(num, mixer3)
        num = prune(num)

        return num

    memo = defaultdict(int)
    for num in nums:
        num = int(num)
        prev = deque([])
        seen = set()
        cur_bananas = num % 10
        for _ in range(2000):
            num = calc(num)
            new_bananas = num % 10 
            prev.append(new_bananas - cur_bananas)
            cur_bananas = new_bananas
            if len(prev) == 4:
                if tuple(prev) not in seen:
                    memo[tuple(prev)] += new_bananas
                    seen.add(tuple(prev))
                prev.popleft()


    return max(memo.values())

print(part2())
