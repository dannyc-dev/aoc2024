from collections import defaultdict

with open('input.txt') as file:
    rules, updates = file.read().split("\n\n")

rules_graph = defaultdict(set)
for rule in rules.split("\n"):
    b, a = rule.split("|")
    rules_graph[a].add(b)

incorrect = []

def part1():
    ans = 0
    for update in updates.split("\n"):
        if not update:
            continue
        update_split = update.split(",")
        seen = set()
        for page in update_split:
            if seen - rules_graph[page]:
                incorrect.append(update_split)
                break
            seen.add(page)
        else:
            mid = len(update_split) // 2
            ans += int(update_split[mid])

    return ans

part1()

def part2():
    def topo(i, possible):
        if i in visited:
            return True

        visited.add(i)

        for j in rules_graph[i].intersection(possible):
            topo(j, possible)

        out.append(i)
        return True


    count = 0
    for update in incorrect:
        out = []
        visited = set()
        possible = set(update)
        for i in update:
            if i in visited:
                continue
            topo(i, possible)
        
        count += int(out[(len(update) // 2)])
    return count
print(part2())


