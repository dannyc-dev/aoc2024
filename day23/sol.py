from functools import cache
from collections import defaultdict


with open('input.txt') as f:
    comps = f.read().split("\n")
    comps = [c.split("-") for c in comps if c.strip()]


def part1():
    graph = defaultdict(lambda: set())
    for left, right in comps:
        graph[left].add(right)
        graph[right].add(left)
    
    out = set()
    for node, children in graph.items():
        if node.startswith('t'):
            tmp = [node]
            for c in children:
                tmp.append(c)
                ins = graph[c] & children
                if ins:
                    for c2 in ins:
                        tmp.append(c2)
                        out.add(tuple(sorted(tmp)))
                        tmp.pop()
                tmp.pop() 
    return len(out)
            

# print(part1())

def part2():
    graph = defaultdict(lambda: set())
    for left, right in comps:
        graph[left].add(right)
        graph[right].add(left)
    
    @cache
    def dfs(node, visited):
        visited ^= set([node])
        
        longest_path = set()
        longest_path_len = 0
        for nn in graph[node]:
            if visited.issubset(graph[nn]):
                path = dfs(nn, visited)
                if len(path) > longest_path_len:
                    longest_path_len = len(path)
                    longest_path = path 

        return longest_path if longest_path else visited
    
    longest_path = []
    longest_path_len = 0
    for node in graph:
        path = dfs(node, frozenset())
        if len(path) > longest_path_len:
            longest_path_len = len(path)
            longest_path = sorted(path)

    return ",".join(longest_path)
print(part2())
